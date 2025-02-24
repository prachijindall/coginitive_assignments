import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

listt = {10, 20, 30, 40, 50}
my_list = list(listt)
my_list[0], my_list[2] = my_list[2], my_list[0]
listt = set(my_list)
print(listt)

