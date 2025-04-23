# Copyright (c) 2018-2022, NVIDIA Corporation
# All rights reserved.

from protomotions.envs.base_env.env_utils.terrains.terrain import Terrain
import math
import numpy as np
from protomotions.envs.base_env.env_utils.terrains.terrain_config import TerrainConfig
from protomotions.envs.base_env.env_utils.terrains.subterrain import SubTerrain
from protomotions.envs.base_env.env_utils.terrains.subterrain_generator import pyramid_sloped_subterrain


class SlopeTerrain(Terrain):
    def __init__(self, config: TerrainConfig, num_envs: int, device) -> None:
        config.load_terrain = False
        config.save_terrain = False
        
        # Minimal terrain settings
        config.num_levels = 1
        config.num_terrains = 1
        
        # Call the parent constructor
        super().__init__(config, num_envs, device)

    def generate_subterrains(self):
        # Clear the fields
        self.walkable_field_raw[:] = 0
        self.flat_field_raw[:] = 0
        
        # Generate a simple slope for each terrain tile
        for j in range(self.env_rows):
            for i in range(self.env_cols):
                # Get the terrain tile coordinates
                start_x = self.border + i * self.width_per_env_pixels
                end_x = self.border + (i + 1) * self.width_per_env_pixels
                start_y = self.border + j * self.length_per_env_pixels
                end_y = self.border + (j + 1) * self.length_per_env_pixels
                
                # Create a subterrain for this tile
                subterrain = SubTerrain(self.config, terrain_name="slope", device=self.device)
                
                # Generate very gentle slope (much gentler than default)
                slope = 0.1  # Small slope value for gentle incline
                platform_size = 3.0  # Size of flat area at the center
                
                # Create a simple sloped terrain
                pyramid_sloped_subterrain(
                    subterrain,
                    slope=slope,
                    platform_size=platform_size
                )
                
                # Copy the subterrain to the main terrain
                self.height_field_raw[start_x:end_x, start_y:end_y] = subterrain.height_field_raw
        
        # Mark borders as non-walkable (this is how the parent class does it)
        self.walkable_field_raw[: self.border, :] = 1
        self.walkable_field_raw[:, -(self.border + self.object_playground_cols + self.object_playground_buffer_size) :] = 1
        self.walkable_field_raw[:, : self.border] = 1
        self.walkable_field_raw[-self.border :, :] = 1
