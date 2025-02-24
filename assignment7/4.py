import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

list = [1, 2, 3, 4, 5]
temp = list[1]
list[1] = list[3]
list[3] = temp
print(list)