# Awesome 3D Topo Benchmark (Related Papers)

This repo curates papers, datasets, and benchmarks for evaluating **3D / topological structure reasoning** in **vision-language(-action) models and embodied agents**.  
We focus on topology-flavored capabilities such as continuity, separation, order, enclosure, holes, and knot/entanglement reasoning.
Contributions are very welcome — please feel free to open an issue or submit a PR.

## Table of Contents

- [Foundations / Methods](#foundations--methods)
  - [Cognitive and Developmental Foundations](#cognitive-and-developmental-foundations)
  - [Topological Task Analysis](#topological-task-analysis)
  - [Mathematical Formalization](#mathematical-formalization)
- [Benchmarks / Datasets by Ability](#benchmarks--datasets-by-ability)
  - [Cross-Ability / Spatial Taxonomy](#cross-ability--spatial-taxonomy)
  - [Continuity](#continuity)
  - [Separation](#separation)
  - [Order](#order)
  - [Enclosure](#enclosure)
  - [Holes](#holes)
  - [Knot / Entanglement](#knot--entanglement)
- [Model Diagnostics](#model-diagnostics)
- [Tools / Environments](#tools--environments)
- [Others](#others)

---

## Foundations / Methods

Papers that justify the taxonomy or define the topological concepts used by the benchmark.

### Cognitive and Developmental Foundations

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| Piaget & Inhelder, [*The Child's Conception of Space*](https://api.pageplace.de/preview/DT0400.9781136220722_A23815605/preview-9781136220722_A23815605.pdf) | Foundational cognitive-development account of topological, projective, and Euclidean spatial concepts, including proximity, separation, order, enclosure, and surrounding. | 1948, 1956 | — |
| Beth & Piaget, [*Mathematical Epistemology and Psychology*](https://books.google.com/books/about/Mathematical_Epistemology_and_Psychology.html?id=3C540QEACAAJ) | Epistemological account of mathematical structures and the psychology of logico-mathematical thought. | 1966 | — |
| Papert, [*Mindstorms: Children, Computers, and Powerful Ideas*](https://www.media.mit.edu/publications/mindstorms/) | Constructionist account of children building mathematical ideas through computational objects-to-think-with. | 1980 | — |

### Topological Task Analysis

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| Martin, [An Analysis of Some of Piaget's Topological Tasks from a Mathematical Point of View](https://www.jstor.org/stable/748762) | Compares Piaget's spatial-concept tasks with mathematical/topological concepts and highlights terminology mismatches. | 1976 | — |
| Strohecker, [*Why Knot?*](https://www.carolstrohecker.info/PapersByYear/1991/WhyKnotDiss.pdf) | Doctoral dissertation on learning topology through knot-tying and media-rich construction environments. | 1991 | — |
| [Understanding Topological Relationships through Comparisons of Similar Knots](http://www.carolstrohecker.info/PapersByYear/1996/UnderstandTopological.pdf) | Learning topology via comparing similar knots, with emphasis on neighborhood, continuity, and boundary. | 1996 | — |
| Gärdenfors, P. *Conceptual Spaces: The Geometry of Thought* (MIT Press), Ch. 3 “Topological and Geometric Properties” | Defines connectedness for regions; argues natural properties are connected; introduces convexity criterion for concepts. | 2000 | — |

### Mathematical Formalization

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| Hatcher, [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf) | Standard algebraic topology reference for homology, holes, enclosure by spheres, and formal separation results such as the Jordan Curve Theorem. | 2002 | — |

---

## Benchmarks / Datasets by Ability

Papers, datasets, and environments that can directly inspire benchmark items or baselines.

| Ability | Static Perception | Temporal Consistency | Intervention / Planning |
|---|---|---|---|
| Continuity | Maze reachability, Möbius continuity, connected components | Object/path continuity across views or frames | Pipe connection, route planning |
| Separation | Shape/object separation, disjoint components | Maintaining separated objects under motion | One-stroke color grouping, partition actions |
| Order | Origami state order, beam-string spatial order, stacking order | Recovering action/order sequence from video | Hanoi Tower, reordering tasks |
| Enclosure | Inside/outside, closed boundary, hole detection, nested containers | Containment persistence under viewpoint or object motion | Laser game, containment manipulation |
| Holes | Hole/tunnel/cavity detection, genus or Euler-characteristic checks, CAD hole features | Hole preservation under view, deformation, reconstruction, or generation | Peg-in-hole insertion, topology-preserving CAD/mesh editing |
| Knot | Closed loop vs. open rope, knot/link detection, chain count | Knot state consistency across deformation | Rope untangling, link manipulation |

### Cross-Ability / Spatial Taxonomy

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [TopoBench: Benchmarking LLMs on Hard Topological Reasoning](https://arxiv.org/abs/2603.12133) | ![TopoBench: Benchmarking LLMs on Hard Topological Reasoning](imgs/topobench_benchmarking_llms_on_hard_topological_reasoning.png) | 2026-03 | [Github](https://github.com/mayug/topobench-benchmark) |
| [Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration? (ICLR 2026)](https://arxiv.org/abs/2602.07055) | ![Theory of Space: Can Foundation Models Construct Spatial Beliefs through Active Exploration? (ICLR 2026)](imgs/theory_of_space_can_foundation_models_construct_spatial_beliefs_thro.png) | 2026-02 | [Github](https://github.com/mll-lab-nu/Theory-of-Space) |
| [Thinking in Structures: Evaluating Spatial Intelligence through Reasoning on Constrained Manifolds](https://arxiv.org/abs/2602.07864) | ![Thinking in Structures: Evaluating Spatial Intelligence through Reasoning on Constrained Manifolds](imgs/thinking_in_structures_evaluating_spatial_intelligence_through_reaso.png) | 2026-02 | [Project](https://ssi-bench.github.io/) |
| [OmniSpatial: Towards Comprehensive Spatial Reasoning Benchmark for Vision Language Models (ICLR 2026)](https://openreview.net/forum?id=6nZKT2rL0H) | ![OmniSpatial benchmark overview.](imgs/omnispatial.png) <!-- Large-scale VLM benchmark with dynamic reasoning, complex spatial logic, spatial interaction, perspective-taking, containment, and inside/outside-style spatial relation tasks. --> | 2026-01 | [Github](https://github.com/qizekun/omnispatial) |
| [ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction (ICLR 2026)](https://arxiv.org/abs/2511.20937) | ![ENACT: Evaluating Embodied Cognition with World Modeling of Egocentric Interaction (ICLR 2026)](imgs/enact_evaluating_embodied_cognition_with_world_modeling_of_egocentri.png) | 2025-11 | [Github](https://github.com/mll-lab-nu/ENACT) |
| [SPATIAL-DISE: A Unified Benchmark for Evaluating Spatial Reasoning in Vision-Language Models](https://arxiv.org/pdf/2510.13394) | ![Unified diagnostic benchmark for spatial reasoning tasks.](imgs/spatial_dise_vlm.png) | 2025-10 | [Dataset](https://huggingface.co/datasets/TACPS-liv/Spatial-DISE) |
| [SITE: towards Spatial Intelligence Thorough Evaluation (ICCV 2025)](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_SITE_towards_Spatial_Intelligence_Thorough_Evaluation_ICCV_2025_paper.html) | ![SITE: towards Spatial Intelligence Thorough Evaluation (ICCV 2025)](imgs/site_towards_spatial_intelligence_thorough_evaluation.png) | 2025-10 | — |
| [3DSRBench: A Comprehensive 3D Spatial Reasoning Benchmark (ICCV 2025)](https://3dsrbench.github.io/) | ![3DSRBench: A Comprehensive 3D Spatial Reasoning Benchmark (ICCV 2025)](imgs/3dsrbench_a_comprehensive_3d_spatial_reasoning_benchmark.png) | 2025-10 | [Project](https://3dsrbench.github.io/) |
| [Can Multimodal Large Language Models Understand Spatial Relations? (ACL 2025)](https://aclanthology.org/2025.acl-long.31/) | ![Can Multimodal Large Language Models Understand Spatial Relations? (ACL 2025)](imgs/can_multimodal_large_language_models_understand_spatial_relations.png) | 2025-07 | [Dataset](https://huggingface.co/datasets/liuziyan/SpatialMQA) |
| [MindCube: Spatial Mental Modeling from Limited Views (ICLR 2026)](https://arxiv.org/abs/2506.21458) | ![MindCube: Spatial Mental Modeling from Limited Views (ICLR 2026)](imgs/mindcube_spatial_mental_modeling_from_limited_views.png) | 2025-06 | [Github](https://github.com/mll-lab-nu/MindCube) |
| [Mind the Gap: Benchmarking Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2503.19707) | ![Benchmarking spatial reasoning in VLMs across synthetic and real images.](imgs/mind_gap_spatial_reasoning_vlm.png) | 2025-03 | [Github](https://github.com/stogiannidis/srbench) |
| [Open3D-VQA: A Benchmark for Comprehensive Spatial Reasoning with Multimodal Large Language Model in Open Space](https://arxiv.org/abs/2503.11094) | ![Open3D-VQA: aerial/open-space spatial reasoning benchmark.](imgs/open3d_mllm.png) | 2025-03 | [Github](https://github.com/EmbodiedCity/Open3D-VQA.code) |
| [RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](https://openreview.net/forum?id=Sextl6R3Nf) | ![RoboSpatial: Teaching Spatial Understanding to 2D and 3D Vision-Language Models for Robotics](imgs/robospatial_teaching_spatial_understanding_to_2d_and_3d_vision_langu.png) | 2025-02 | — |
| [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents (ICML 2025)](https://arxiv.org/abs/2502.09560) | ![EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents (ICML 2025)](imgs/embodiedbench_comprehensive_benchmarking_multi_modal_large_language.png) | 2025-02 | [Github](https://github.com/EmbodiedBench/EmbodiedBench) |
| [LayoutVLM: Differentiable Optimization of 3D Layout via Vision-Language Models (CVPR 2025)](https://arxiv.org/abs/2412.02193) | ![LayoutVLM: Differentiable Optimization of 3D Layout via Vision-Language Models (CVPR 2025)](imgs/layoutvlm_differentiable_optimization_of_3d_layout_via_vision_langua.png) | 2024-12 | [Github](https://github.com/sunfanyunn/LayoutVLM) |
| [Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making (NeurIPS 2024 D&B)](https://arxiv.org/abs/2410.07166) | ![Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making (NeurIPS 2024 D&B)](imgs/embodied_agent_interface_benchmarking_llms_for_embodied_decision_mak.png) | 2024-10 | [Github](https://github.com/embodied-agent-interface/embodied-agent-interface) |
| [ScanQA: 3D Question Answering for Spatial Scene Understanding](https://arxiv.org/abs/2112.10482) | ![3D question answering with object-grounded answers and 3D bounding boxes.](imgs/scan3d_vlm.png) | 2021-12 | [Github](https://github.com/ATR-DBI/ScanQA) |

### Continuity

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [TDBench: Benchmarking Vision-Language Models in Understanding Top-Down Images](https://arxiv.org/abs/2504.03748) | ![Benchmarking VLMs on top-down imagery.](imgs/tdbench_vlm.png) | 2025-04 | — |
| [AlphaMaze: Enhancing Large Language Models' Spatial Intelligence via GRPO](https://arxiv.org/abs/2502.14669) | ![AlphaMaze](imgs/alpha_maze.png) | 2025-02 | — |
| [Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces](https://arxiv.org/abs/2412.14171) | ![Video-based visual-spatial intelligence benchmark (VSI-Bench).](imgs/space_mllm.png) | 2024-12 | [Github](https://github.com/vision-x-nyu/thinking-in-space) |
| [AMaze: An intuitive benchmark generator for fast prototyping of generalizable agents](https://arxiv.org/abs/2411.13072) | ![Procedural maze generator to study generalization under deceptive cues.](imgs/amaze.png) | 2024-11 | — |
| [Topological Planning with Transformers for Vision-and-Language Navigation (CVPR 2021)](https://arxiv.org/abs/2012.05292) | ![Predicts interpretable navigation plans on topological maps from language instructions.](imgs/topo_plannning_vln.png) | 2021 | — |

### Separation

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [Enhancing Spatial Reasoning in Multimodal Large Language Models through Reasoning-based Segmentation (ICCV 2025)](https://openaccess.thecvf.com/content/ICCV2025/html/Ning_Enhancing_Spatial_Reasoning_in_Multimodal_Large_Language_Models_through_Reasoning-based_ICCV_2025_paper.html) | ![Enhancing Spatial Reasoning in Multimodal Large Language Models through Reasoning-based Segmentation (ICCV 2025)](imgs/enhancing_spatial_reasoning_in_multimodal_large_language_models_thro.png) | 2025-10 | — |
| [Rel3D: A Minimally Contrastive Benchmark for Grounding Spatial Relations in 3D (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/file/76dc611d6ebaafc66cc0879c71b5db5c-Paper.pdf) | ![Rel3D: A Minimally Contrastive Benchmark for Grounding Spatial Relations in 3D (NeurIPS 2020)](imgs/rel3d_a_minimally_contrastive_benchmark_for_grounding_spatial_relati.png) | 2020 | [Github](https://github.com/princeton-vl/Rel3D) |

### Order

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| TBD | TBD | — | — |

### Enclosure

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [Visual Spatial Reasoning](https://aclanthology.org/2023.tacl-1.37/) | ![Visual Spatial Reasoning](imgs/visual_spatial_reasoning.png) | 2023 | [Dataset](https://huggingface.co/datasets/cambridgeltl/vsr_random) |
| [Rel3D: A Minimally Contrastive Benchmark for Grounding Spatial Relations in 3D (NeurIPS 2020)](https://proceedings.neurips.cc/paper/2020/file/76dc611d6ebaafc66cc0879c71b5db5c-Paper.pdf) | ![Rel3D: A Minimally Contrastive Benchmark for Grounding Spatial Relations in 3D (NeurIPS 2020)](imgs/rel3d_a_minimally_contrastive_benchmark_for_grounding_spatial_relati.png) | 2020 | [Github](https://github.com/princeton-vl/Rel3D) |

### Holes

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [EvoCAD: Evolutionary CAD Code Generation with Vision Language Models](https://arxiv.org/abs/2510.11631) | ![EvoCAD: Evolutionary CAD Code Generation with Vision Language Models](imgs/evocad_evolutionary_cad_code_generation_with_vision_language_models.png) | 2025-10 | — |
| [VideoCAD: A Large-Scale Video Dataset for Learning UI Interactions and 3D Reasoning from CAD Software](https://arxiv.org/abs/2505.24838) | ![VideoCAD: A Large-Scale Video Dataset for Learning UI Interactions and 3D Reasoning from CAD Software](imgs/videocad_a_large_scale_video_dataset_for_learning_ui_interactions_an.png) | 2025-05 | [Github](https://github.com/BrandonMan123/VideoCAD) |
| [Zero-Shot Peg Insertion: Identifying Mating Holes and Estimating SE(2) Poses with Vision-Language Models](https://arxiv.org/abs/2503.06026) | ![Zero-Shot Peg Insertion: Identifying Mating Holes and Estimating SE(2) Poses with Vision-Language Models](imgs/zero_shot_peg_insertion_identifying_mating_holes_and_estimating_se_p.png) | 2025-03 | — |
| [Euler Characteristic Transform Based Topological Loss for Reconstructing 3D Images From Single 2D Slices (CVPRW 2023)](https://openaccess.thecvf.com/CVPR2023_workshops/TAG-PRA) | ![Euler Characteristic Transform Based Topological Loss for Reconstructing 3D Images From Single 2D Slices (CVPRW 2023)](imgs/euler_characteristic_transform_based_topological_loss_for_reconstruc.png) | 2023-06 | — |
| [BRepNet: A Topological Message Passing System for Solid Models (CVPR 2021)](https://openaccess.thecvf.com/content/CVPR2021/html/Lambourne_BRepNet_A_Topological_Message_Passing_System_for_Solid_Models_CVPR_2021_paper.html) | ![BRepNet: A Topological Message Passing System for Solid Models (CVPR 2021)](imgs/brepnet_a_topological_message_passing_system_for_solid_models.png) | 2021 | [Github](https://github.com/AutodeskAILab/BRepNet) |

### Knot / Entanglement

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [Knot So Simple: A Minimalistic Environment for Spatial Reasoning](https://arxiv.org/abs/2505.18028) | ![Knot So Simple](imgs/knot_so_simple.png) | 2025-05 | [Github](https://github.com/lil-lab/knotgym) |
| [Untangling Dense Non-Planar Knots by Learning Manipulation Features and Recovery Policies](https://arxiv.org/abs/2107.08942) | ![Learned manipulation features and recovery policies for dense knot untangling.](imgs/untangle_manipulation.png) | 2021-07 | [Website](https://sites.google.com/berkeley.edu/non-planar-untangling) |
| [Untangling Dense Knots by Learning Task-Relevant Keypoints](https://arxiv.org/abs/2011.04999) | ![Learned keypoints guide a geometric planner to untangle dense knots.](imgs/untangle_keypoint.png) | 2020-11 | — |
| [Learning to Manipulate Deformable Objects without Demonstrations](https://arxiv.org/abs/1910.13439) | ![Deformable object manipulation for rope and cloth tasks.](imgs/manipulate_deformable.png) | 2019-10 | — |
| [10K Knots (Kaggle)](https://www.kaggle.com/datasets/josephcameron/10knots) | ![10k-knots](imgs/10k_knot.png) | 2018 | — |

---

## Model Diagnostics

Papers that reveal strengths or failures of MLLMs, VLMs, VLA systems, and video generative models on topological structure.

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [VisRes Bench: On Evaluating the Visual Reasoning Capabilities of VLMs](https://arxiv.org/html/2512.21194v1) | ![Image-only benchmark for perceptual and rule-based visual reasoning.](imgs/visres_vlm.png) | 2025-12 | — |
| [Generalizing Shape-from-Template to Topological Changes (STAG 2025)](https://arxiv.org/abs/2511.03459) | ![Shape-from-template generalized to topological changes like cuts and tears.](imgs/topo_change.png) | 2025-11 | — |
| [OPTiCAL: An Abstract Positional Reasoning Benchmark for Vision Language Models](https://ufdatastudio.com/papers/driggers-ellis2025optical.pdf) | ![Abstract positional reasoning with shapes.](imgs/optical_vlm.png) | 2025 | [Github](https://github.com/ufdatastudio/optical?tab=readme-ov-file) |
| [Computer Vision Models Show Human-Like Sensitivity to Geometric and Topological Concepts](https://arxiv.org/abs/2505.13281) | ![Odd-one-out diagnostic for geometric and topological concepts.](imgs/topo_concept.png) | 2025-05 | — |
| [Revisiting 3D LLM Benchmarks: Are We Really Testing 3D Capabilities? (ACL Findings 2025)](https://arxiv.org/abs/2502.08503) | ![Diagnosing “2D-cheating” in 3D LLM benchmark evaluation.](imgs/revisit_3d_llm.png) | 2025-02 | — |

---

## Tools / Environments

Implementation references used to build, render, or operationalize benchmark tasks.

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| [Handle-based Mesh Deformation Guided By Vision Language Model](https://arxiv.org/abs/2506.04562) | ![Training-free handle-based mesh deformation guided by a VLM.](imgs/mesh_deform_vlm.png) | 2025-06 | — |
| [three.js](https://threejs.org) | ![WebGL 3D library often used for rendering/visualization.](imgs/three_js.png) | — | [Github](https://github.com/mrdoob/three.js/) |
| [Physically Grounded Vision-Language Models for Robotic Manipulation](https://ieeexplore.ieee.org/document/10610090) | ![Robot planning pipeline combining LLM planning with VLM concept querying.](imgs/robo_manipulation_vlm.png) | — | — |

---

## Others

Relevant papers that provide adjacent motivation but do not directly define the taxonomy, produce benchmark tasks, diagnose models, or support implementation.

| Title | Introduction | Date | Code |
|---|---|---:|:---:|
| TBD | TBD | — | — |
