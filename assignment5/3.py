import pandas as pd
import numpy as np
x=153
sales=np.array([x,x+50,x+100,x+150,x+200])
print(sales)

#3.b
print(sales*(1+((x%5)+5)/100))

#3.c
print(np.where(sales<x+100,sales*0.95,sales*0.90))

#3.d
matrix=np.tile(sales,(3,1))
print(matrix)

final=np.arange(3).reshape(3,1)
increase=matrix*(1+0.02*final)
print(increase)

