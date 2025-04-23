#!/bin/bash

# Add memory optimization
#export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

# Set your IsaacLab path
ISAAC_LAB_PATH="/home/subho/Projects/Robotics/IsaacLab/isaaclab.sh"
PYTHON_PATH="$ISAAC_LAB_PATH -p"

# Set the path to the pretrained MaskedMimic checkpoint
CHECKPOINT_PATH="data/pretrained_models/masked_mimic/smpl/last.ckpt"

# Set the motion file path
MOTION_FILE="data/motions/smpl_humanoid_walk.npy"

# Run with complex terrain and record the simulation
$PYTHON_PATH protomotions/eval_agent.py \
  +robot=smpl \
  +simulator=isaaclab \
  +motion_file=$MOTION_FILE \
  +checkpoint=$CHECKPOINT_PATH \
  +terrain=flat \
  +record=True 