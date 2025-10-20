# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

from .base_spectra import BaseSpectra

class IRSpectra(BaseSpectra):
    def __init__(self, 
                 yLabel:str = "Transmittance (T)",
                 yUnit:str = "%",
                 xLabel:str = "Wavenumber",
                 yQty:str = "Transmittance",
                 xQty:str = "wavenumber",
                 xUnit:str = ""):
        super().__init__(yLabel, yUnit, xLabel, yQty, xQty, xUnit)
    
    def validateDataset(self):
        raise NotImplementedError("Not yet implemented")

    def visualizeSpectra(self):
        raise NotImplementedError("Not yet implemented")