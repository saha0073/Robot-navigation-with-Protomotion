#!/bin/bash

# Memory optimization
export LD_LIBRARY_PATH=${CONDA_PREFIX}/lib/

# Set your IsaacLab path
ISAAC_LAB_PATH="/home/subho/Projects/Robotics/IsaacLab/isaaclab.sh"
PYTHON_PATH="$ISAAC_LAB_PATH -p"

# Set the path to the pretrained MaskedMimic checkpoint
CHECKPOINT_PATH="data/pretrained_models/masked_mimic/smpl/last.ckpt"

# Set the motion file path
MOTION_FILE="data/motions/smpl_humanoid_walk.npy"

# Run with maximum CPU offloading
$PYTHON_PATH protomotions/eval_agent.py \
  +robot=smpl \
  +simulator=isaaclab \
  +motion_file=$MOTION_FILE \
  +checkpoint=$CHECKPOINT_PATH \
  +terrain=flat2 \
  +simulator.gpu_physics=False \
  +task.env.num_envs=1 \
  +simulator.force_cpu=True \
  +simulator.headless_caching=False \
  +simulator.render_gpu_id=-1 \
  +simulator.device=cpu \
  ++precision=32 \
  ++agent.config.device=cpu 