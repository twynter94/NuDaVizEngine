# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

from .base_spectra import BaseSpectra

class UVVisSpectra(BaseSpectra):
    def __init__(self, 
                 yLabel:str = "Absorbance (A)",
                 yUnit:str = "ndim",
                 xLabel:str = "Wavelength (nm)",
                 yQty:str = "abs",
                 xQty:str = "wavelength",
                 xUnit:str = "nm"):
        super().__init__(yLabel, yUnit, xLabel, yQty, xQty, xUnit)
    
    def validateDataset(self):
        raise NotImplementedError("Not yet implemented")

    def visualizeSpectra(self):
        raise NotImplementedError("Not yet implemented")
    
    def generateTaucPlot(self):
        raise NotImplementedError("Not yet implemented")