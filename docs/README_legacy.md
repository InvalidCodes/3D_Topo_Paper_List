# 3D TopoBench — Paper Investigation Scope

Internal reference for the project team and Codex context windows.
For the public paper list, see [`README.md`](../README.md).

---

## Purpose

This repo collects related papers for **3D TopoBench**, a benchmark for evaluating 3D topological reasoning in MLLMs and embodied agents.
We focus on *qualitative structural understanding* (connected? inside? knotted?) rather than metric geometry (how far? how big?).

---

## Classification Principle

Use a three-level classification when adding or reviewing papers:

1. **Role** — why the paper matters to this benchmark.
2. **Ability** — which topological ability it supports or evaluates.
3. **Evaluation mode** — whether it is static perception, temporal consistency, or intervention/planning.

This avoids mixing foundational theory papers with benchmark papers and implementation tools.

| Level | Options | Use for |
| --- | --- | --- |
| Role | Foundations / Methods, Benchmarks / Datasets, Model Diagnostics, Tools / Environments, Others | Deciding the top-level section |
| Ability | Continuity, Separation, Order, Enclosure, Knot | Deciding the benchmark task family |
| Evaluation mode | Static perception, Temporal consistency, Intervention / planning | Deciding the task format |

---

## Paper Categories

### 1. Foundations / Methods

Papers that justify the benchmark taxonomy or define topological concepts used by tasks.

#### Cognitive and Developmental Foundations

- **Chen Lin (1982) "Topology-First"** — argues that the human visual system perceives topological properties such as connectivity, holes, and inside/outside before local geometric properties such as shape, size, and orientation.
- **Spelke's Object Principles** — infants reason with solidity and spatiotemporal continuity; these map naturally to no self-intersection, no tearing, and object persistence under motion.
- **Piaget & Inhelder (1948/1956), *The Child's Conception of Space*** — developmental account of topological, projective, and Euclidean spatial concepts, including proximity, separation, order, and enclosure.
- **Beth & Piaget (1966), *Mathematical Epistemology and Psychology*** — epistemological framing for mathematical structures and logico-mathematical thought.
- **Papert (1980), *Mindstorms*** — constructionist account of building mathematical ideas through computational objects-to-think-with.

#### Topological Task Analysis

- **J. Larry Martin (1976), "An Analysis of Some of Piaget's Topological Tasks from a Mathematical Point of View"** — compares Piagetian spatial tasks with mathematical topology and clarifies where cognitive and mathematical terms diverge.
- **C. Strohecker (1991), "Why Knot?"** — studies how proximity, continuity, connection, separation, and order enter into children's thinking about knots.
- **Gärdenfors (2000), *Conceptual Spaces*, Ch. 3** — defines connectedness for conceptual regions and motivates topology-like structure in concept representation.

#### Mathematical Formalization

- **Hatcher (2002), *Algebraic Topology*, Ch. 2** — formalizes cycles, holes, homology, and separation; useful for grounding hole and enclosure tasks.
- **Hatcher (2002), §2.B, Jordan Curve Theorem** — formalizes enclosure as a closed boundary separating an interior from an exterior.

### 2. Benchmarks / Datasets by Ability

Papers, datasets, and environments that can directly inspire benchmark items or baselines.

| Ability | Static Perception | Temporal Consistency | Intervention / Planning |
| --- | --- | --- | --- |
| Continuity | Maze reachability, Möbius continuity, connected components | Object/path continuity across views or frames | Pipe connection, route planning |
| Separation | Shape/object separation, disjoint components | Maintaining separated objects under motion | One-stroke color grouping, partition actions |
| Order | Origami state order, beam-string spatial order, stacking order | Recovering action/order sequence from video | Hanoi Tower, reordering tasks |
| Enclosure | Inside/outside, closed boundary, hole detection, nested containers | Containment persistence under viewpoint or object motion | Laser game, containment manipulation |
| Knot | Closed loop vs. open rope, knot/link detection, chain count | Knot state consistency across deformation | Rope untangling, link manipulation |

Current collection targets:

- **Connectivity / Continuity** — maze and graph-style reachability benchmarks, topological navigation, path planning.
- **Enclosure / Holes** — inside/outside and missing-interior reasoning, including 2D boundaries and 3D shells.
- **Knot / Entanglement** — rope, knot, link, and chain topology, especially tasks where geometry changes but topology should remain invariant.
- **Geometric and Topological Diagnostics** — VLM tests that include topological invariants, visual odd-one-out tasks, or topological change detection.

### 3. Model Diagnostics

Papers that reveal strengths or failures of MLLMs, VLMs, VLA systems, and video generative models on topological structure.

Key questions:

- Do models preserve topology under viewpoint changes, deformation, or temporal evolution?
- Do they distinguish metric geometry from qualitative structure?
- Do video models respect solidity, continuity, enclosure, and non-self-intersection?
- Can a model reason about an intervention that changes geometry without changing topology?

### 4. Tools / Environments

Implementation references used to build or render benchmark tasks.

- [three.js docs](https://threejs.org/docs) — browser-based 3D rendering.
- [three-csg-ts](https://github.com/samalexander/three-csg-ts) — CSG operations for constructing enclosure, holes, and Boolean geometry tasks.
- Rope, cloth, and deformable-object simulators — useful for knot and entanglement interventions.

### 5. Others

Relevant papers that provide adjacent motivation but do not directly define the taxonomy, produce benchmark tasks, diagnose models, or support implementation.

Examples:

- General spatial reasoning papers without explicit topological structure.
- Broad cognitive-science papers where topology is only a minor example.
- Robotics or graphics papers that use 3D geometry but do not test topological invariants.

---

## Add-Paper Decision Rules

When a new paper is added, assign one primary category and optional secondary tags.

1. If it explains **why the taxonomy exists**, put it under **Foundations / Methods**.
2. If it provides a **task, dataset, benchmark, or environment**, put it under **Benchmarks / Datasets by Ability**.
3. If it analyzes **model behavior or failure modes**, put it under **Model Diagnostics**.
4. If it is mostly useful for **building the benchmark**, put it under **Tools / Environments**.
5. If it is relevant but weakly connected, put it under **Others**.

For benchmark papers, always tag the ability family: `Continuity`, `Separation`, `Order`, `Enclosure`, or `Knot`.

---

## Investigation Questions

- Does the paper test viewpoint-invariant or deformation-invariant structure?
- Does it go beyond left/right/distance and evaluate qualitative relationships?
- Does it contain tasks that can be rendered or simulated in 3D?
- Does it isolate topological reasoning from language priors or metric shortcuts?
- Does it provide a useful failure mode for current MLLMs, VLMs, VLA systems, or video models?
