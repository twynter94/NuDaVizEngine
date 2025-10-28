# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

import pandas as pd

def loadDatasetFromCSV(filePath:str) -> pd.DataFrame:
    df = pd.read_csv(filepath_or_buffer=filePath,
                     encoding="UTF-16")
    return df