# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

from abc import ABC, abstractmethod
from nudavizengine.dataset import Dataset

class BaseVisualizer(ABC):
    def __init__(self):
        self._figure = object()
        self._axes = object()

    @abstractmethod
    def generateLinePlot(self, datasets:list[Dataset], xQty:str, yQty:str):
        pass

    @abstractmethod
    def generateScatterPlot(self, dataset:list[Dataset]):
        pass

    @abstractmethod
    def saveFig(self):
        pass