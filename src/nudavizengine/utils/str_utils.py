# BSD 3-Clause License
# Copyright (c) 2025, Theodore Wynter, NanoUncovered
# All rights reserved.
#
# This source code is licensed under the BSD 3-Clause License found in the
# LICENSE file in the root directory of this source tree.

import re

def findMatch(inputString:str, regex:str):
    match = re.search(regex, inputString)
    if match:
        return True
    else:
        return False
    
def mergeStrings(str1:str, str2:str):
    return f"{str.lower(str1).replace(" ", "_")}_{str.lower(str2).replace(" ", "_")}"