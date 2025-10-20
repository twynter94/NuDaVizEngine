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

from nudavizengine.scientific_data.spectroscopy.uvvis_spectra import UVVisSpectra
from nudavizengine.dataset.dataset import Dataset
from nudavizengine.dataset.uvvis_dataset_hp8453 import UVVisDatasetHP8453

# Public API
__all__ = [
    "Dataset",
    "UVVisSpectra",
    "UVVisDatasetHP8453"
]

#package-level initialization code
print(f"NUDaVizEngine v{__version__} loaded!")