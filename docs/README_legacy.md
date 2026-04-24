# 3D TopoBench — Paper Investigation Scope

Internal reference for the project team and Codex context windows.
For the public paper list, see [`README.md`](../README.md).

---

## Purpose

This repo collects related papers for **3D TopoBench**, a benchmark for evaluating 3D topological reasoning in MLLMs and embodied agents.
We focus on *qualitative structural understanding* (connected? inside? knotted?) rather than metric geometry (how far? how big?).

---

## Investigation Directions

### 1. Cognitive Literature

Foundational theories of how humans perceive and reason about topology.

- **Chen Lin (1982) "Topology-First"** — the human visual system perceives topological properties (connectivity, holes, inside/outside) *before* local geometric ones (shape, size, orientation).
- **Spelke's Object Principles** — infants understand the physical world via *Solidity* (no self-intersection) and *Spatiotemporal Continuity* (no tearing), which map directly onto topological invariants.
- Piaget & Inhelder (1948/1956) — developmental account of topological, projective, and Euclidean spatial concepts in children.
- Gärdenfors (2000) *Conceptual Spaces* — connectedness of regions; convexity criterion for natural concepts.

#### Papers Supporting Taxonomy

These papers ground the benchmark's task categories (proximity, continuity, connection, separation, order, enclosure) in cognitive and mathematical literature.

Taxonomy structure (Piaget lineage):

- **Piaget & Inhelder (1948, 1956), Beth & Piaget (1966), Papert (1980)** — describe the epistemological structures of topology (proximity, continuity, connection, separation), order (seriation), and classification, which together contribute to the emergence of mathematical thinking.
- **C. Strohecker, "Why Knot?" (1991)** — shows how these deep structures (proximity, continuity, connection, separation, order) enter into thinking about knots; formulates a way of characterizing differences in terms of an implicit preference for one or another of the structures.
- **J. Larry Martin, "An Analysis of Some of Piaget's Topological Tasks from a Mathematical Point of View" (1976)** — notions of proximity and separation complement one another in their development; awareness of separation allows the child to take into account different degrees of proximity.

#### Papers Supporting Holes in Enclosure

These papers justify treating *holes* as a subtype of *enclosure* and define the relationship formally.

- **Piaget & Inhelder (1956) *The Child's Conception of Space*, Ch.1 §4** — "In three dimensions enclosure takes the form of the relation of 'insideness', as in the case of an object in a closed box." (Enclosure = inside/outside perception ability.)
- **Hatcher (2002) *Algebraic Topology*, Ch.2 p.100** — "This spherical cycle detects the presence of a 'hole' in X₃, the missing interior of the sphere. However, since this hole is enclosed by a sphere rather than a circle, it is of a different sort." (Standard algebraic topology textbook defines "hole" directly using "enclosed" and "missing interior".)
- **Hatcher (2002), §2.B p.169 (Jordan Curve Theorem)** — "A subspace of S² homeomorphic to S¹ separates S² into two complementary components." (Mathematical formalization of enclosure: a closed boundary → interior + exterior.)

### 2. Spatial Works (especially benchmarks)

Benchmarks evaluating spatial reasoning in VLMs/MLLMs, with emphasis on structural/relational tasks.

Key questions: Does the benchmark test viewpoint-invariant structure? Does it go beyond left/right/distance?

### 3. Topology Works

Papers that explicitly handle topological properties in vision, geometry processing, or robot perception.

Key questions: Genus/Betti number estimation, knot/link detection, topological invariance under deformation, persistent homology applied to visual scenes.

### 4. MLLMs and Video Generative Models

How current multimodal models handle (or fail at) topological structure, and what video generation models reveal about 3D structural understanding.

Key questions: Do MLLMs maintain topological consistency across views? Do video models respect solidity and continuity?

---

## Task Scope (for paper relevance)

| Ability | Static Perception | Intervention / Planning |
| --- | --- | --- |
| Continuity | Maze/Möbius, reachability A→B | Pipe connection env |
| Separation | Shape/object separation detection | One-stroke color grouping |
| Order | Origami (time order), beam string (spatial order) | Hanoi Tower |
| Enclosure | Hole detection, 2D/3D enclosure | Laser game |
| Knot | Closed loop vs. knot, chain count | Untangle env |

---

## Related Materials

- [three.js docs](https://threejs.org/docs)
- [three-csg-ts](https://github.com/samalexander/three-csg-ts) — CSG for three.js
