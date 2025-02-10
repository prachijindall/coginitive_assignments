import numpy as np
array=np.array([10,52,62,16,16,54,453])
print(array)

#2.1
print(np.sort(array))

#2.2
print(np.argsort(array))

#2.3
print(np.partition(array,4)[:4])

#2.4
print(np.partition(array,-5)[-5:])

