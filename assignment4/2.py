import numpy as np
arr=np.array([1,2,3,6,4,5])
print(arr)

#2.a
arr1=arr[::-1]
print(arr1)

#2.b.1
x=np.array([1,2,3,4,5,1,2,1,1,1])
unique,counts=np.unique(x,return_counts=True)
count_index=np.argmax(counts)
freqval=unique[count_index]
freqcount=counts[count_index]
print(freqval)
indices=np.where(x==freqval)[0]
print(indices)

y=np.array([1,1,1,2,3,4,2,4,3,3])

uniquey,countss=np.unique(y,return_counts=True)
count_indexy=np.argmax(countss)
freqvaly=uniquey[count_indexy]
freqcounty=countss[count_indexy]
print(freqvaly)
indicess=np.where(y==freqvaly)[0]
print(indicess)

