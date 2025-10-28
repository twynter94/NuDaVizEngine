# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

from nudavizengine.visualizers.base_visualizer import BaseVisualizer
from nudavizengine.visualizers.visualizer_registry import VisualizerRegistry
from nudavizengine.dataset import Dataset
import matplotlib as mpl
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

@VisualizerRegistry.register("matplotlib", "MatplotLib plotting engine.")
class MatplotlibVisualizer(BaseVisualizer):
    def __init__(self, **kwargs):
        self._figure, self._axes = plt.subplots()

    def generateLinePlot(self, datasets:list[Dataset], xQty:str, yQty:str):
        for dataset in datasets:
            logger.debug("Get quantity for x-axis")
            xData = dataset.getDataForQuantity(xQty)
            yData = dataset.getDataForQuantity(yQty)
            self._axes.plot(xData, yData)
        plt.show()
            

    def generateScatterPlot(self, dataset:list[Dataset]):
        pass

    def saveFig(self):
        pass
