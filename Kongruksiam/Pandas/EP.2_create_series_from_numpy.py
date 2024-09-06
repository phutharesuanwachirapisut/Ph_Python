# Series = array 1D
# DataFrame = array 2D
# Panel = array 3D

import pandas as pd
import numpy as np

data_ls = [10,20,"sesa","ipad",True]
ndata = np.array(data_ls)

print("pandas series from array = {0}, data type = {1}".format(pd.Series(ndata), ndata.dtype))
