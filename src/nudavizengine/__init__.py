# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

__version__ = "0.0.1"

"""
NUDaVizEngine: NanoUncovered Data Visualization Engine

This package provides tools for plotting and analyzing scientific data from
both experimental and computational techniques. It includes classes for
common experimental techniques (UV-Vis, IR, etc.) and computational data
(Band Structure, Density of States, etc.).

Top-level imports are provided for convenience.
"""

from nudavizengine.scientific_data import UVVisSpectra
from nudavizengine.dataset import Dataset, UVVisDatasetHP8453
from nudavizengine.visualizers import MatplotlibVisualizer, BaseVisualizer, VisualizerRegistry

# Public API
__all__ = [
    "Dataset",
    "UVVisSpectra",
    "UVVisDatasetHP8453"
]

#package-level initialization code
print(f"NUDaVizEngine v{__version__} loaded!")

#Visualization engines supported currently
print(f"Visualization engines available: \n\n{VisualizerRegistry.showRegistry()}")