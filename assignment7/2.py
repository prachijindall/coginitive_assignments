import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
array = np.array([[1, -2, 3], [-4, 5, -6]])
print(np.abs(array))
print("Flattened:", np.percentile(array, [25, 50, 75]))
print("Column-wise:", np.percentile(array, [25, 50, 75], axis=0))
print("Row-wise:", np.percentile(array, [25, 50, 75], axis=1))
print("Flattened:", [np.mean(array), np.median(array), np.std(array)])
print("Column-wise:", [np.mean(array, axis=0), np.median(array, axis=0), np.std(array, axis=0)])
print("Row-wise:", [np.mean(array, axis=1), np.median(array, axis=1), np.std(array, axis=1)])