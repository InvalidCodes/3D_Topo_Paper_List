#!/usr/bin/env python3
"""Extract caption-free Figure 1 images for README paper rows.

The script is intentionally conservative: it scans README table rows, processes
rows whose introduction cell does not already contain an image, downloads a PDF
when a paper link can be resolved, crops the graphic area above the Figure 1
caption, trims surrounding whitespace, saves the result under imgs/, and updates
the README image cell.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
import time
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import parse_qs, quote, unquote, urljoin, urlparse

warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL.*")

try:
    import fitz  # PyMuPDF
    import requests
    from PIL import Image
except ImportError as exc:
    missing = getattr(exc, "name", "dependency")
    raise SystemExit(
        f"Missing {missing}. Install dependencies with: "
        "python3 -m pip install -r requirements.txt"
    ) from exc


CAPTION_START_RE = re.compile(r"^\s*(?:fig(?:ure)?\.?)\s*1\b", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
PDF_LINK_RE = re.compile(
    r"""(?:href|content)=["']([^"']+?\.pdf(?:\?[^"']*)?)["']""",
    re.IGNORECASE,
)
META_PDF_RE = re.compile(
    r"""<meta[^>]+name=["']citation_pdf_url["'][^>]+content=["']([^"']+)["']""",
    re.IGNORECASE,
)
ARXIV_ID_RE = re.compile(
    r"""(?:arxiv\.org/(?:abs|pdf)/|arxiv[:\s]+)(\d{4}\.\d{4,5})(?:v\d+)?""",
    re.IGNORECASE,
)


@dataclass
class PaperRow:
    line_index: int
    line: str
    title_cell: str
    intro_cell: str
    date_cell: str
    code_cell: str
    title: str
    url: str
    slug: str


@dataclass
class ExtractResult:
    ok: bool
    message: str
    image_path: Path | None = None
    pdf_url: str | None = None


def split_markdown_row(line: str) -> list[str] | None:
    if not line.startswith("|"):
        return None
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    if len(cells) != 4:
        return None
    return cells


def strip_markdown(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return " ".join(text.split())


def slugify(text: str, max_len: int = 68) -> str:
    text = strip_markdown(text).lower()
    text = re.sub(r"\([^)]*\)", "", text)
    text = re.sub(r"[^a-z0-9]+", "_", text).strip("_")
    text = re.sub(r"_+", "_", text)
    return (text[:max_len].rstrip("_") or "paper")


def parse_readme(
    readme_path: Path,
    match: str | None = None,
    include_existing_images: bool = False,
    include_foundations: bool = False,
) -> tuple[list[str], list[PaperRow]]:
    lines = readme_path.read_text(encoding="utf-8").splitlines()
    matcher = re.compile(match, re.IGNORECASE) if match else None
    rows: list[PaperRow] = []

    current_h2 = ""
    for idx, line in enumerate(lines):
        h2_match = re.match(r"^##\s+(.+?)\s*$", line)
        if h2_match:
            current_h2 = h2_match.group(1)

        if not line.startswith("| "):
            continue
        if current_h2 == "Foundations / Methods" and not include_foundations:
            continue
        if line.startswith("|---") or line.startswith("| Title") or line.startswith("| Ability"):
            continue

        cells = split_markdown_row(line)
        if not cells:
            continue
        title_cell, intro_cell, date_cell, code_cell = cells
        if title_cell.upper() == "TBD":
            continue
        if IMAGE_RE.search(intro_cell) and not include_existing_images:
            continue

        match_obj = MARKDOWN_LINK_RE.search(title_cell)
        if not match_obj:
            continue

        title = strip_markdown(match_obj.group(1))
        url = match_obj.group(2)
        if matcher and not matcher.search(f"{title} {url}"):
            continue

        rows.append(
            PaperRow(
                line_index=idx,
                line=line,
                title_cell=title_cell,
                intro_cell=intro_cell,
                date_cell=date_cell,
                code_cell=code_cell,
                title=title,
                url=url,
                slug=slugify(title),
            )
        )

    return lines, rows


def arxiv_id_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    if "arxiv.org" not in parsed.netloc:
        return None

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) >= 2 and parts[0] in {"abs", "pdf", "html"}:
        arxiv_id = parts[1]
    elif parts:
        arxiv_id = parts[-1]
    else:
        return None

    arxiv_id = arxiv_id.removesuffix(".pdf")
    return arxiv_id if re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", arxiv_id) else None


def candidate_pdf_urls(url: str) -> list[str]:
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    path = parsed.path
    candidates: list[str] = []

    arxiv_id = arxiv_id_from_url(url)
    if arxiv_id:
        candidates.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")

    if "openreview.net" in host:
        query = parse_qs(parsed.query)
        if "id" in query:
            candidates.append(f"https://openreview.net/pdf?id={quote(query['id'][0])}")

    if "aclanthology.org" in host:
        candidates.append(url.rstrip("/") + ".pdf")

    if "openaccess.thecvf.com" in host and "/html/" in path and path.endswith(".html"):
        prefix, file_name = url.split("/html/", 1)
        candidates.append(f"{prefix}/papers/{file_name[:-5]}.pdf")

    if path.lower().endswith(".pdf"):
        candidates.append(url)

    unique: list[str] = []
    for candidate in candidates:
        if candidate not in unique:
            unique.append(candidate)
    return unique


def score_pdf_candidate(pdf_url: str, title: str) -> int:
    haystack = unquote(pdf_url).lower()
    tokens = [
        token
        for token in re.findall(r"[a-z0-9]+", strip_markdown(title).lower())
        if len(token) >= 5
        and token
        not in {
            "paper",
            "papers",
            "benchmark",
            "benchmarks",
            "towards",
            "through",
            "based",
            "using",
            "large",
            "language",
            "models",
            "vision",
        }
    ]
    return sum(1 for token in tokens if token in haystack)


def scrape_pdf_urls(url: str, session: requests.Session, title: str) -> list[str]:
    try:
        response = session.get(url, timeout=25)
        response.raise_for_status()
    except requests.RequestException:
        return []

    content_type = response.headers.get("content-type", "").lower()
    if "application/pdf" in content_type or response.content[:4] == b"%PDF":
        return [url]

    text = response.text
    urls: list[str] = []
    for regex in (META_PDF_RE, PDF_LINK_RE):
        for match in regex.findall(text):
            absolute = urljoin(url, match)
            if absolute not in urls:
                urls.append(absolute)

    arxiv_ids = sorted(set(ARXIV_ID_RE.findall(text)))
    if len(arxiv_ids) == 1:
        arxiv_pdf = f"https://arxiv.org/pdf/{arxiv_ids[0]}.pdf"
        if arxiv_pdf not in urls:
            urls.append(arxiv_pdf)

    if len(urls) <= 1:
        return urls

    scored = sorted(
        ((score_pdf_candidate(pdf_url, title), pdf_url) for pdf_url in urls),
        reverse=True,
    )
    if scored[0][0] == 0:
        return []
    return [pdf_url for score, pdf_url in scored if score > 0]


def download_pdf(url: str, title: str, cache_dir: Path, session: requests.Session) -> tuple[Path, str]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    attempts = candidate_pdf_urls(url)
    attempts.extend(scrape_pdf_urls(url, session, title))

    seen: set[str] = set()
    errors: list[str] = []
    for pdf_url in attempts:
        if pdf_url in seen:
            continue
        seen.add(pdf_url)
        cache_name = quote(pdf_url, safe="").replace("%", "_") + ".pdf"
        cache_path = cache_dir / cache_name
        if cache_path.exists() and cache_path.stat().st_size > 1024:
            return cache_path, pdf_url

        try:
            response = session.get(pdf_url, timeout=45)
            response.raise_for_status()
        except requests.RequestException as exc:
            errors.append(f"{pdf_url}: {exc}")
            continue

        content = response.content
        if content[:4] != b"%PDF":
            errors.append(f"{pdf_url}: not a PDF")
            continue

        cache_path.write_bytes(content)
        time.sleep(0.2)
        return cache_path, pdf_url

    detail = "; ".join(errors[-3:]) if errors else "no PDF URL found"
    raise RuntimeError(detail)


def text_from_block(block: dict) -> str:
    parts: list[str] = []
    for line in block.get("lines", []):
        for span in line.get("spans", []):
            parts.append(span.get("text", ""))
        parts.append(" ")
    return "".join(parts).strip()


def find_caption_blocks(page: fitz.Page) -> list[fitz.Rect]:
    captions: list[fitz.Rect] = []
    text = page.get_text("dict")
    for block in text.get("blocks", []):
        if block.get("type") != 0:
            continue
        block_text = text_from_block(block)
        if CAPTION_START_RE.search(block_text):
            captions.append(fitz.Rect(block["bbox"]))
    return captions


def horizontal_overlap(a: fitz.Rect, b: fitz.Rect) -> float:
    overlap = max(0.0, min(a.x1, b.x1) - max(a.x0, b.x0))
    return overlap / max(1.0, min(a.width, b.width))


def figure_column(page_rect: fitz.Rect, caption: fitz.Rect) -> fitz.Rect:
    margin = max(16.0, page_rect.width * 0.035)
    if caption.width >= page_rect.width * 0.55:
        return fitz.Rect(
            page_rect.x0 + margin,
            page_rect.y0,
            page_rect.x1 - margin,
            page_rect.y1,
        )

    mid_x = (page_rect.x0 + page_rect.x1) / 2
    gutter = page_rect.width * 0.025
    if (caption.x0 + caption.x1) / 2 < mid_x:
        return fitz.Rect(page_rect.x0 + margin, page_rect.y0, mid_x - gutter, page_rect.y1)
    return fitz.Rect(mid_x + gutter, page_rect.y0, page_rect.x1 - margin, page_rect.y1)


def graphical_rects(page: fitz.Page) -> list[fitz.Rect]:
    rects: list[fitz.Rect] = []

    for image in page.get_images(full=True):
        xref = image[0]
        try:
            rects.extend(page.get_image_rects(xref))
        except Exception:
            continue

    try:
        drawings = page.get_drawings()
    except Exception:
        drawings = []

    for drawing in drawings:
        rect = fitz.Rect(drawing.get("rect"))
        if rect.is_empty or rect.width < 2 or rect.height < 2:
            continue
        if rect.width * rect.height < 12:
            continue
        rects.append(rect)

    return rects


def rect_union(rects: Iterable[fitz.Rect]) -> fitz.Rect | None:
    iterator = iter(rects)
    try:
        union = fitz.Rect(next(iterator))
    except StopIteration:
        return None
    for rect in iterator:
        union.include_rect(rect)
    return union


def infer_figure_rect(page: fitz.Page, caption: fitz.Rect) -> fitz.Rect | None:
    page_rect = page.rect
    column = figure_column(page_rect, caption)
    search_top = max(page_rect.y0 + 20, caption.y0 - page_rect.height * 0.72)
    search_area = fitz.Rect(column.x0, search_top, column.x1, caption.y0 - 3)

    all_candidates: list[fitz.Rect] = []
    seed_candidates: list[fitz.Rect] = []
    for rect in graphical_rects(page):
        if rect.y1 > caption.y0 + 2 or rect.y0 < search_top:
            continue
        if rect.width > page_rect.width * 0.96 and rect.height < 6:
            continue
        all_candidates.append(rect)
        if horizontal_overlap(rect, search_area) >= 0.15 or search_area.contains(rect.tl):
            seed_candidates.append(rect)

    if seed_candidates:
        # Keep the vertically connected graphical cluster closest to the
        # caption. This captures multi-panel figures whose panels are
        # horizontally disconnected while avoiding older content farther above.
        seed_candidates.sort(key=lambda rect: rect.y1, reverse=True)
        anchor = seed_candidates[0]
        cluster = [anchor]
        current_top = anchor.y0
        max_vertical_gap = max(42.0, page_rect.height * 0.075)
        for rect in sorted(all_candidates, key=lambda item: item.y1, reverse=True):
            if rect == anchor:
                continue
            vertical_gap = current_top - rect.y1
            if vertical_gap <= max_vertical_gap:
                cluster.append(rect)
                current_top = min(current_top, rect.y0)

        fig_rect = rect_union(cluster)
        if fig_rect:
            pad = 8
            bottom_pad = 18
            page_margin = max(8.0, page_rect.width * 0.015)
            fig_rect = fitz.Rect(
                max(page_rect.x0 + page_margin, fig_rect.x0 - pad),
                max(page_rect.y0, fig_rect.y0 - pad),
                min(page_rect.x1 - page_margin, fig_rect.x1 + pad),
                min(caption.y0 - 2, fig_rect.y1 + bottom_pad),
            )
            if fig_rect.width >= 80 and fig_rect.height >= 60:
                return fig_rect

    fallback_height = min(page_rect.height * 0.38, 290)
    fallback = fitz.Rect(
        column.x0,
        max(page_rect.y0 + 20, caption.y0 - fallback_height),
        column.x1,
        caption.y0 - 4,
    )
    return fallback if fallback.width >= 80 and fallback.height >= 60 else None


def trim_whitespace(image: Image.Image, threshold: int = 248, padding: int = 2) -> Image.Image:
    rgb = image.convert("RGB")
    pixels = rgb.load()
    width, height = rgb.size
    xs: list[int] = []
    ys: list[int] = []

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if min(r, g, b) < threshold:
                xs.append(x)
                ys.append(y)

    if not xs or not ys:
        return rgb

    left = max(0, min(xs) - padding)
    upper = max(0, min(ys) - padding)
    right = min(width, max(xs) + padding + 1)
    lower = min(height, max(ys) + padding + 1)
    return remove_top_island(rgb.crop((left, upper, right, lower)), threshold=threshold)


def remove_top_island(image: Image.Image, threshold: int = 248) -> Image.Image:
    """Drop isolated header text accidentally captured above a figure."""
    rgb = image.convert("RGB")
    pixels = rgb.load()
    width, height = rgb.size
    if height < 160:
        return rgb

    min_row_pixels = max(3, int(width * 0.004))
    row_counts: list[int] = []
    for y in range(height):
        count = 0
        for x in range(width):
            if min(pixels[x, y]) < threshold:
                count += 1
        row_counts.append(count)

    dark_rows = [idx for idx, count in enumerate(row_counts) if count >= min_row_pixels]
    if len(dark_rows) < 2:
        return rgb

    min_gap = max(18, int(height * 0.035))
    for prev_row, next_row in zip(dark_rows, dark_rows[1:]):
        gap = next_row - prev_row
        if gap < min_gap or next_row > height * 0.28:
            continue
        top_dark = sum(row_counts[: prev_row + 1])
        bottom_dark = sum(row_counts[next_row:])
        if bottom_dark and top_dark < bottom_dark * 0.12:
            return rgb.crop((0, max(0, next_row - 2), width, height))

    return rgb


def render_crop(page: fitz.Page, rect: fitz.Rect, out_path: Path, zoom: float) -> None:
    pixmap = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=rect, alpha=False)
    image = Image.open(io.BytesIO(pixmap.tobytes("png")))
    image = trim_whitespace(image)
    if image.width < 120 or image.height < 80:
        raise RuntimeError(f"crop too small after trimming: {image.width}x{image.height}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(out_path, optimize=True)


def extract_figure_one(pdf_path: Path, out_path: Path, max_pages: int, zoom: float) -> None:
    doc = fitz.open(pdf_path)
    try:
        limit = min(max_pages, len(doc))
        caption_candidates: list[tuple[int, fitz.Rect]] = []
        for page_index in range(limit):
            page = doc[page_index]
            for caption in find_caption_blocks(page):
                caption_candidates.append((page_index, caption))

        if not caption_candidates:
            raise RuntimeError("Figure 1 caption not found")

        last_error: Exception | None = None
        for page_index, caption in caption_candidates:
            page = doc[page_index]
            fig_rect = infer_figure_rect(page, caption)
            if not fig_rect:
                continue
            try:
                render_crop(page, fig_rect, out_path, zoom)
                return
            except Exception as exc:
                last_error = exc

        raise RuntimeError(str(last_error) if last_error else "could not infer figure crop")
    finally:
        doc.close()


def image_markdown(title: str, path: Path) -> str:
    alt = title.replace("|", " ").replace("[", "").replace("]", "")
    return f"![{alt}]({path.as_posix()})"


def rebuild_row(row: PaperRow, intro: str) -> str:
    return f"| {row.title_cell} | {intro} | {row.date_cell} | {row.code_cell} |"


def process_row(
    row: PaperRow,
    out_dir: Path,
    cache_dir: Path,
    session: requests.Session,
    max_pages: int,
    zoom: float,
    overwrite: bool,
) -> ExtractResult:
    image_path = out_dir / f"{row.slug}.png"
    if image_path.exists() and not overwrite:
        return ExtractResult(True, "image already exists", image_path=image_path)

    try:
        pdf_path, pdf_url = download_pdf(row.url, row.title, cache_dir, session)
        extract_figure_one(pdf_path, image_path, max_pages=max_pages, zoom=zoom)
        return ExtractResult(True, "extracted", image_path=image_path, pdf_url=pdf_url)
    except Exception as exc:
        return ExtractResult(False, str(exc), image_path=None)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract Figure 1 images for README papers.")
    parser.add_argument("--readme", default="README.md", type=Path)
    parser.add_argument("--out-dir", default="imgs", type=Path)
    parser.add_argument("--cache-dir", default=".cache/fig1", type=Path)
    parser.add_argument("--match", help="Only process rows whose title or URL matches this regex.")
    parser.add_argument("--max-pages", default=6, type=int, help="Pages to scan from each PDF.")
    parser.add_argument("--zoom", default=2.5, type=float, help="PDF render scale.")
    parser.add_argument("--overwrite", action="store_true", help="Regenerate existing target PNGs.")
    parser.add_argument(
        "--include-foundations",
        action="store_true",
        help="Also process rows under Foundations / Methods.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Show rows that would be processed.")
    parser.add_argument(
        "--no-update-readme",
        action="store_true",
        help="Extract images without rewriting README rows.",
    )
    args = parser.parse_args()

    readme_path = args.readme
    lines, rows = parse_readme(
        readme_path,
        match=args.match,
        include_existing_images=args.overwrite,
        include_foundations=args.include_foundations,
    )
    if not rows:
        print("No missing-image paper rows found.")
        return 0

    if args.dry_run:
        for row in rows:
            print(f"would process: {row.title} -> {args.out_dir / (row.slug + '.png')}")
        return 0

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 fig1-extractor "
                "(https://github.com/yunfei/3d-topo-paper-list)"
            )
        }
    )

    updated = 0
    failures = 0
    for row in rows:
        result = process_row(
            row=row,
            out_dir=args.out_dir,
            cache_dir=args.cache_dir,
            session=session,
            max_pages=args.max_pages,
            zoom=args.zoom,
            overwrite=args.overwrite,
        )
        if result.ok and result.image_path:
            rel_path = result.image_path.relative_to(readme_path.parent)
            intro = image_markdown(row.title, rel_path)
            if not args.no_update_readme:
                lines[row.line_index] = rebuild_row(row, intro)
                updated += 1
            source = f" from {result.pdf_url}" if result.pdf_url else ""
            print(f"OK  {row.title}: {rel_path}{source}", flush=True)
        else:
            failures += 1
            print(f"SKIP {row.title}: {result.message}", file=sys.stderr, flush=True)

    if updated and not args.no_update_readme:
        readme_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Done. Updated rows: {updated}. Failed/skipped: {failures}.")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
