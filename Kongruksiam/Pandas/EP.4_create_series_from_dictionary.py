# Series = array 1D
# DataFrame = array 2D
# Panel = array 3D

import pandas as pd
import numpy as np
# dicitonary = {value:key}

data_dict = {"grape":50 , "banana":20, "water melon": 130}
print("pandas series from dictionary = {}".format(pd.Series(data_dict)))
