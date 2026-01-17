# Awesome 3D Topo Benchmark (Related Papers)

This repo curates papers, datasets, and benchmarks for evaluating **3D / topological structure reasoning** in **vision-language(-action) models and embodied agents**.  
We focus on topology-flavored capabilities such as connectivity, enclosure/separation, holes, and entanglement.  
Contributions are very welcome — please feel free to open an issue or submit a PR.

## Table of Contents
- [Methods](#methods)
- [Datasets & Benchmarks](#datasets--benchmarks)
  - [Connectivity](#connectivity)
  - [Enclosure & Separation](#enclosure--separation)
  - [Holes](#holes)
  - [Entanglement](#entanglement)
  - [Geometric & Topological Concept Diagnostics](#geometric--topological-concept-diagnostics)
- [Findings & Applications](#findings--applications)
- [Appendix](#appendix)
  - [Text-only / Symbolic Baselines (LLM)](#text-only--symbolic-baselines-llm)
  - [Tools](#tools)

---

## Methods

| Title | Introduction | Date | Code |
|---|---|---:|:---:|


---

## Datasets & Benchmarks

All tables are sorted by **time (newest first)**.

### Connectivity

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [AMaze: An intuitive benchmark generator for fast prototyping of generalizable agents](https://arxiv.org/abs/2411.13072) | ![Procedural maze generator to study generalization under deceptive cues.](imgs/amaze.png) | 2024-11 | — |
| [Topological Planning with Transformers for Vision-and-Language Navigation (CVPR 2021)](https://arxiv.org/abs/2012.05292) | ![Predicts interpretable navigation plans on topological maps from language instructions.](imgs/topo_plannning_vln.png) | 2021 | — |

### Enclosure & Separation

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| TBD | TBD | — | — |

### Holes

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| TBD | TBD | — | — |

### Entanglement

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [Knot So Simple: A Minimalistic Environment for Spatial Reasoning](https://arxiv.org/abs/2505.18028) | ![Knot So Simple](imgs/knot_so_simple.png) | 2025-05 | [Github](https://github.com/lil-lab/knotgym) |
| [10K Knots (Kaggle)](https://www.kaggle.com/datasets/josephcameron/10knots) | ![10k-knots](imgs/10k_knot.png) | 2018 | — |

### Geometric & Topological Concept Diagnostics

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [Computer Vision Models Show Human-Like Sensitivity to Geometric and Topological Concepts](https://arxiv.org/abs/2505.13281) | ![Odd-one-out diagnostic for geometric and topological concepts.](imgs/topo_concept.png) | 2025-05 | — |

---

## Findings & Applications

TBD.

---

## Appendix

### Text-only / Symbolic Baselines (LLM)

Used to isolate reasoning/planning from visual perception.

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [AlphaMaze: Enhancing Large Language Models' Spatial Intelligence via GRPO](https://arxiv.org/abs/2502.14669) | ![aplha-maze](imgs/alpha_maze.png) | 2025-02 | — |

### Tools

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [Handle-based Mesh Deformation Guided By Vision Language Model](https://arxiv.org/abs/2506.04562) | ![Training-free handle-based mesh deformation guided by a VLM.](imgs/mesh_deform_vlm.png) | 2025-06 | — |
| [three.js](https://threejs.org) | ![WebGL 3D library often used for rendering/visualization.](imgs/three_js.png) | — | [Github](https://github.com/mrdoob/three.js/) |
| [Physically Grounded Vision-Language Models for Robotic Manipulation](https://ieeexplore.ieee.org/document/10610090) | ![Robot planning pipeline combining LLM planning with VLM concept querying.](imgs/robo_manipulation_vlm.png) | — | — |