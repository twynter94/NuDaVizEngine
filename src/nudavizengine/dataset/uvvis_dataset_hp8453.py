# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

from nudavizengine.dataset.dataset import Dataset

class UVVisDatasetHP8453(Dataset):
    def __init__(self,
                 filePath:str,
                 src:str = "HP8453",
                 xCol:tuple[str,str,int] = ("Wavelength", "nm", 1),
                 yCol1:tuple[str,str,int] = ("Absorbance", "", 2),
                 yCol2:tuple[str,str,int]=("Absorbance Standard deviation", "", 3)) -> None:
        super().__init__(filePath, src, xCol, yCol1, yCol2=yCol2)
        