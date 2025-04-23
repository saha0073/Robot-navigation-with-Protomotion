# Copyright (c) 2018-2022, NVIDIA Corporation
# All rights reserved.

from protomotions.envs.base_env.env_utils.terrains.terrain import Terrain
import math
import numpy as np
from protomotions.envs.base_env.env_utils.terrains.terrain_config import TerrainConfig
from protomotions.envs.base_env.env_utils.terrains.subterrain import SubTerrain
from protomotions.envs.base_env.env_utils.terrains.subterrain_generator import pyramid_stairs_subterrain


class StairsTerrain(Terrain):
    def __init__(self, config: TerrainConfig, num_envs: int, device) -> None:
        # Don't modify the original config too much - this was causing dimension mismatches
        config.load_terrain = False
        config.save_terrain = False
        
        # We still want minimal terrain
        config.num_levels = 1
        config.num_terrains = 1
        
        # Call the parent constructor
        super().__init__(config, num_envs, device)

    def generate_subterrains(self):
        # Clear the fields
        self.walkable_field_raw[:] = 0
        self.flat_field_raw[:] = 0
        
        # Generate a simple staircase
        for j in range(self.env_rows):
            for i in range(self.env_cols):
                # Get the terrain tile coordinates
                start_x = self.border + i * self.width_per_env_pixels
                end_x = self.border + (i + 1) * self.width_per_env_pixels
                start_y = self.border + j * self.length_per_env_pixels
                end_y = self.border + (j + 1) * self.length_per_env_pixels
                
                # Create a subterrain for this tile
                subterrain = SubTerrain(self.config, terrain_name="stairs", device=self.device)
                
                # Generate simple stairs
                step_width = 0.7  # Wider steps (meters)
                step_height = 0.03  # Lower steps (meters)
                platform_size = 3.0  # Larger platform (meters)
                
                # Create stairs
                pyramid_stairs_subterrain(
                    subterrain,
                    step_width=step_width,
                    step_height=step_height,
                    platform_size=platform_size
                )
                
                # Copy the subterrain to the main terrain
                self.height_field_raw[start_x:end_x, start_y:end_y] = subterrain.height_field_raw
        
        # Mark borders as non-walkable
        self.walkable_field_raw[: self.border, :] = 1
        self.walkable_field_raw[:, -(self.border + self.object_playground_cols + self.object_playground_buffer_size) :] = 1
        self.walkable_field_raw[:, : self.border] = 1
        self.walkable_field_raw[-self.border :, :] = 1