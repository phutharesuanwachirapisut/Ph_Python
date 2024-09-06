# Series = array 1D
# DataFrame = array 2D
# Panel = array 3D

import pandas as pd
import numpy as np

data_ls = [10,20,"sesa","ipad",True]
print("pandas series from list = {}".format(pd.Series(data_ls)))

data_tp = (10,20,"sesa","ipad",True)
print("pandas series from tuple = {}".format(pd.Series(data_tp)))
# index  Element Value
# 0      10
# 1      20
# 2    sesa
# 3    ipad
# 4    True