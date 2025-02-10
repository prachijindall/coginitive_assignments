import numpy as np
gfg=np.matrix('[4,1,9;12,3,1;4,5,6]')
print(gfg)

#1.1
print(np.sum(gfg))

#1.2
print(np.sum(gfg,axis=1))

#1.3
print(np.sum(gfg,axis=0))