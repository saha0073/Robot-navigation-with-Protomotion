### ProtoMotions-Extended-Terrain-Demos

This repository extends NVIDIA's ProtoMotions framework with custom terrain implementations and demo scripts for physics-based character animation. It focuses on demonstrating the MaskedMimic algorithm for humanoid robot navigation in various environments.

![Demo Preview](output/renderings/maskedmimic-2025-04-18-12-51-16%20-%20Trim.gif) <!-- Demo GIF -->

## Features
- **Custom Terrain Implementations**: Extended the original terrain system with slope-based and stair-based terrains
- **Optimized Demo Scripts**: Created scripts for running demos with different memory optimization techniques

## Overview
MaskedMimic is a powerful algorithm for physics-based character control. It works in two stages:
1. A reinforcement learning model is trained on full-body motion tracking data
2. The model learns to fill in missing movements using partial data

This enables robots to perform complex movements like walking, climbing stairs, or sitting on furniture without retraining from scratch for each task.

## Quick Start

### Prerequisites
- IsaacLab installed
- ProtoMotions dependencies installed
- CUDA-capable GPU

### Running Demos

#### Flat Terrain Demo
![Flat Terrain Demo](output/renderings/maskedmimic-2025-04-18-12-51-16%20-%20Trim.gif)

#### Robot Sitting on Sofa Demo (NVIDIA simulation)
![Robot Sitting on Sofa](assets/sofa.gif)

#### Complex Terrain Navigation Demo (NVIDIA silumation)
![Robot in Complex Terrain](assets/vr-cartwheel.gif)

#### Custom Terrain Demo (with optimizations)

## Key Modifications
- `protomotions/envs/base_env/env_utils/terrains/stairs.py`: Custom stair terrain implementation
- `protomotions/envs/base_env/env_utils/terrains/slope.py`: Custom slope terrain implementation
- `protomotions/config/terrain/custom.yaml`: Configuration for simplified complex terrain

## Technical Challenges
- **GPU Memory Optimization**: Implemented techniques to reduce GPU memory usage for complex terrains
- **Physics Simulation**: Balanced terrain complexity with physics simulation performance
- **Observation Compatibility**: Ensured terrain observations matched the pretrained model expectations

## Results
The demos showcase how MaskedMimic enables humanoid robots to navigate different terrain types while maintaining natural human-like motion. This technology is fundamental to generalist robot systems like NVIDIA's GR00T.

## Acknowledgments
This work builds upon NVIDIA's ProtoMotions framework. All original code and assets belong to their respective owners. 
