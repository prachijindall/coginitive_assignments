import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

arr = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])
print("Floor:", np.floor(arr))
print("Ceiling:", np.ceil(arr))
print("Truncated:", np.trunc(arr))
print("Rounded:", np.round(arr))