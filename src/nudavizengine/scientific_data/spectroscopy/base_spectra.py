# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

from abc import ABC, abstractmethod
from nudavizengine.dataset import Dataset
from nudavizengine.visualizers import MatplotlibVisualizer, VisualizerRegistry, BaseVisualizer

class BaseSpectra(ABC):
    def __init__(self, 
                 visualizerID:str,
                 yLabel:str,
                 yUnit:str,
                 xLabel:str,
                 yQty:str,
                 xQty:str,
                 xUnit:str):
        #set axis labels for the final plot
        self._visualizerID:str = visualizerID
        self._visualizer: BaseVisualizer = VisualizerRegistry.createVisualizer(self._visualizerID)
        self._yLabel:str = yLabel
        self._xLabel:str = xLabel
        #Specify the actual Phsyical quantities and units that are to be on the plot.
        #If data set units do not match what is specified here, then the code will attempt to convert if possible
        self._yQty:str = yQty
        self._yUnit:str = yUnit
        self._xQty:str = xQty
        self._xUnit:str = xUnit
        self._datasets:list[Dataset] = []

    def addDataset(self, dataset: Dataset) -> None:
        self._datasets.append(dataset)

    def describeDatasets(self):
        return [ds.describeData() for ds in self._datasets]

    @classmethod
    def showVisualizers(cls):
        return VisualizerRegistry.showRegistry()
    
    @abstractmethod
    def validateDataset(self):
        pass

    @abstractmethod
    def visualizeSpectra(self, xQty:str, yQty:str):
        pass
    