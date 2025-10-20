# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

from abc import ABC, abstractmethod
from nudavizengine.dataset.dataset import Dataset

class BaseSpectra(ABC):
    def __init__(self, 
                 yLabel:str,
                 yUnit:str,
                 xLabel:str,
                 yQty:str,
                 xQty:str,
                 xUnit:str):
        #set axis labels for the final plot
        self.__yLabel:str = yLabel
        self.__xLabel:str = xLabel
        #Specify the actual Phsyical quantities and units that are to be on the plot.
        #If data set units do not match what is specified here, then the code will attempt to convert if possible
        self.__yQty:str = yQty
        self.__yUnit:str = yUnit
        self.__xQty:str = xQty
        self.__xUnit:str = xUnit
        self.__datasets:list[Dataset] = []

    def addDataset(self, dataset: Dataset) -> None:
        self.__datasets.append(dataset)

    def describeDatasets(self):
        return [ds.describeData() for ds in self.__datasets]
    
    @abstractmethod
    def validateDataset(self):
        pass

    @abstractmethod
    def visualizeSpectra(self):
        pass
    