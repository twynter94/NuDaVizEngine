# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

import logging
logger = logging.getLogger(__name__)

from nudavizengine.visualizers.base_visualizer import BaseVisualizer

class VisualizerRegistry:
    __registry:dict = {}

    @staticmethod
    def register(visualizerID:str,
                 description: str
                 ):
        """Decorator used to register visualization egines"""
        def inner(visualizationClass):
            logger.debug(f"Check if a source with the same name already exists: {visualizerID}")
            if VisualizerRegistry.getVisualizer(visualizerID) is None:
                VisualizerRegistry.__registry[visualizerID.lower()] = {
                    "description": description,
                    "class": visualizationClass
                }
            else:
                raise ValueError(f"A visualizer with the same ID already exists: {visualizerID}")
            
            return visualizationClass
        return inner
    
    @staticmethod
    def createVisualizer(visualizerID: str, **kwargs):
        visualizer = VisualizerRegistry.getVisualizerClass(visualizerID)
        if visualizer is None:
            raise ValueError(f"Visualizer not found for ID: {visualizerID}.\n"
                             f"Available Visualizers: {VisualizerRegistry.showRegistry()}")
        return visualizer(**kwargs)

    @staticmethod
    def getVisualizer(visualizerID:str):
        return VisualizerRegistry.__registry.get(visualizerID, None)
    
    @staticmethod 
    def getVisualizerClass(visualizerID: str):
        visualizerClass = BaseVisualizer
        if VisualizerRegistry.getVisualizer(visualizerID) is not None:
            visualizerClass = VisualizerRegistry.__registry[visualizerID.lower()]["class"]
        else:
            visualizerClass = None
        return visualizerClass
    
    @staticmethod
    def showRegistry():
        return list(VisualizerRegistry.__registry.keys())