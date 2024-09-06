# Series = array 1D
# DataFrame = array 2D
# Panel = array 3D

import pandas as pd
import numpy as np

items = ["grape","banana","water melon"]
print("pandas series = {0}".format(pd.Series(items)))

idx = [50,20,130]
print("pandas series by input index = {0}".format(pd.Series(items,index=idx))) # คล้าย dictionary
