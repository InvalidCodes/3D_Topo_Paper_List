# 3D Topo Benchmark — Related Papers (Awesome List)

This repo curates papers, datasets, and environments for evaluating **3D / topological structure reasoning** in **VLM/VLA/agents**, organized into four task families:
- **Connectivity** (reachability, maze, graph connectivity)
- **Enclosure & Separation** (containment, inside/outside, separability)
- **Holes** (holes, tunnels, layered-structure reasoning)
- **Entanglement** (rope/knot/link topology, crossings, closed loop vs open rope)

## Table of Contents
- [Paper List](#paper-list)
  - [Connectivity](#connectivity)
  - [Enclosure & Separation](#enclosure--separation)
  - [Holes](#holes)
  - [Entanglement](#entanglement)
- [Datasets / Environments](#datasets--environments)
- [How to Add a Paper](#how-to-add-a-paper)

---

## Paper List

### Connectivity
- **MazeEval: A Benchmark for Testing Sequential Decision-Making in Language Models** — arXiv 2025. [[Paper]](https://arxiv.org/abs/2507.20395)  
  - **Focus**: Coordinate-based maze navigation via function calling to isolate spatial reasoning without visual input  
  - **Tags**: benchmark, maze, navigation, LLM, function-calling

- **AlphaMaze: Enhancing Large Language Models' Spatial Intelligence via GRPO** — arXiv 2025. [[Paper]](https://arxiv.org/abs/2502.14669)  
  - **Focus**: Two-stage training (SFT + GRPO) for step-wise maze navigation on tokenized maze representations  
  - **Tags**: maze, navigation, LLM, SFT, GRPO

- **AMaze: An intuitive benchmark generator for fast prototyping of generalizable agents** — arXiv 2024. [[Paper]](https://arxiv.org/abs/2411.13072) [[PDF]](https://arxiv.org/pdf/2411.13072)  
  - **Focus**: A controllable maze/sign generator for evaluating generalization under distribution shifts and deceptive cues  
  - **Tags**: benchmark, procedural generation, generalization, maze, RL

### Enclosure & Separation
- _TODO_

### Holes
- _TODO_

### Entanglement
- **Knot So Simple: A Minimalistic Environment for Spatial Reasoning** — arXiv 2025. [[Paper]](https://arxiv.org/abs/2505.18028)  
  - **Focus**: KnotGym; goal-conditioned rope manipulation from image observations with complexity scaled by the number of crossings  
  - **Tags**: benchmark, rope manipulation, spatial reasoning, generalization

---

## Datasets / Environments
- _TODO_

---

## How to Add a Paper
PRs are welcome. Please update both:
1) `bibliography/references.bib` (BibTeX)
2) `bibliography/papers.yaml` (structured metadata)

See `CONTRIBUTING.md` for the exact format.
