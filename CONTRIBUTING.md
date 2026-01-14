# Contributing Guide

PRs and issues are welcome.

## What to Add
- **Papers**: benchmarks, environments, datasets, or diagnostic tasks related to 3D/topological structure reasoning
- **Datasets / Environments**: reproducible simulators, real-world setups, and public datasets

## How to Add a Paper (Recommended)
Please keep these in sync:
- `README.md`: add the paper under one of the four top-level categories
- `bibliography/papers.yaml`: add a structured entry
- `bibliography/references.bib`: add a BibTeX entry

## Entry Style (README)
Recommended format:
- **Title** — Venue/Type Year. [[Paper]](link) [[PDF]](link) [[Code]](link)  
  - **Focus**: one sentence on what the benchmark/env evaluates  
  - **Tags**: comma-separated keywords (benchmark, env, dataset, generalization, planning, ...)

## Field Conventions (`bibliography/papers.yaml`)
- **key**: lowercase and stable (recommended `lastnameYYYYshortname`)
- **domain**: one or more of `Connectivity` / `Enclosure & Separation` / `Holes` / `Entanglement`
- **links**: provide at least `paper` (abstract page) or `pdf` (direct link); add `code` if available

## Sorting
- Within each category, sort by **year (newest first)** whenever possible.
