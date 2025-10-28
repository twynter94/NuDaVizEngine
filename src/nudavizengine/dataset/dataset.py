# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

import pandas as pd
import logging
logger = logging.getLogger(__name__)
from nudavizengine.utils import getFileType, findMatch, mergeStrings
from nudavizengine.dataset.dataset_io import loadDatasetFromCSV

class Dataset:
    def __init__(self,
                 filePath:str,
                 src:str,
                 xCol:tuple[str,str,int], #(wavelength, nm, 1)
                 yCol1:tuple[str,str,int],
                 **kwargs) -> None:
        self.__filePath:str = filePath
        self.__src:str = src
        self.__data = pd.DataFrame()
        self.__xColName:str = xCol[0]
        self.__xColUnit:str = self.__validateUnit(xCol[1])
        self.__xColNum:int = xCol[2]
        self.__dfKeyList:list = [] #index 0 is for the xCol, other indices are for ycols
        self.__yColList:list[dict] = []
        self.__updateDataDictionary(yCol1, kwargs)
        self.__updateDataKeys()

    def getYCols(self):
        return self.__yColList
    
    def getData(self):
        return self.__data
    
    def describeData(self):
        return self.__data.info()
    
    def getDataForQuantity(self, quantity:str) -> pd.Series | None:
        logger.debug(f"check if the quantity exists in the data frame: {quantity}")
        for dfKey in self.__dfKeyList:
            if findMatch(dfKey, rf"^{quantity.lower()}_\d+"):
                return self.__data[dfKey]
        else:
            return None

    def __updateDataDictionary(self, 
                               yCol1:tuple[str,str,int], 
                               kwargs:dict):
        logger.debug("Update the list of y-columns")
        self.__yColList.append({
                            "yColName": yCol1[0],
                            "yColUnit": self.__validateUnit(yCol1[1]),
                            "yColNum": yCol1[2]
                        })
        if kwargs.keys() != []:
                for key in kwargs.keys():
                    if findMatch(str.lower(key), r"^ycol\d+"):
                        self.__validateYcolInput(key, kwargs.get(key))
                        self.__yColList.append({
                            "yColName": kwargs[key][0],
                            "yColUnit": self.__validateUnit(kwargs[key][1]),
                            "yColNum": kwargs[key][2]
                        })
    
        logger.debug(f"Load dataset from file: {self.__filePath}")
        fileType = getFileType(self.__filePath)
        df = pd.DataFrame
        match(fileType):
            case "csv":
                df = loadDatasetFromCSV(self.__filePath)
            case "txt":
                raise NotImplementedError(f"Support for extension {fileType} is not yet implemented")
            case _:
                raise ValueError("File type not supported")

        if df.empty == False:
            self.__data = df
    
    def __validateYcolInput(self, key:str, yCol) -> None:
        logger.debug("Validate yCol data passed in kwargs to ensure it has the requisite structure")
        expectedSignature = (str, str, int)
        isSuccess = True
        if not isinstance(yCol, tuple):
            isSuccess = False
        elif len(yCol) != len(expectedSignature):
            isSuccess = False
        else:
            for index, signature in enumerate(expectedSignature):
                if not isinstance(yCol[index], signature):
                    isSuccess = False
                    break

        if not isSuccess:
            raise TypeError(f"Invalid input specified for parameter: {key}.\n A tuple is expected with the following signature: {expectedSignature}")

    def updateColumnName(self, colNum:int, colName:str) -> None:
        if colNum <= len(self.__data.columns.tolist()):
            self.__data.rename(columns={self.__data.columns[colNum-1]: colName}, inplace=True)
       
    def __updateDataKeys(self) -> None:
        logger.debug("Create and update column names for the data frame based on user input")
        colName:str = mergeStrings(f"{self.__xColName}_{self.__xColNum}", self.__xColUnit)
        self.__dfKeyList.append(colName)
        self.updateColumnName(self.__xColNum, self.__dfKeyList[0])
        for yColDict in self.__yColList:
            colName = mergeStrings(f"{yColDict["yColName"]}_{yColDict["yColNum"]}", yColDict["yColUnit"])
            self.__dfKeyList.append(colName)
            self.updateColumnName(yColDict["yColNum"], colName)

    def __validateUnit(self, unit: str) -> str:
        logger.debug("Validate units to ensure it is supported")
        #Unit module not yet implemented, for now, replace empty units with ndim - no dimension
        if unit == "":
            return "ndim"
        else:
            return unit