# Series = array 1D
# DataFrame = array 2D
# Panel = array 3D

import pandas as pd
import numpy as np
# dicitonary = {value:key}

data_dict = {"grape":50 , "banana":20, "water melon": 130}
print("Price of grape = {}".format(pd.Series(data_dict["grape"]))) # เหมือนการเรียนใช้ Dictionary ทั่วไป
print("Price of banana = {}".format(pd.Series(data_dict["banana"]))) # seem like recession of dicitonary
print("Price of water melon = {}".format(pd.Series(data_dict["water melon"])))
