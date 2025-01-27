import numpy as np
import pandas as pd
dict1={"id":[1,2,3,4,5,6,7,8,9,10],
    "refund":["yes","no","no","yes","no","no","yes","no","no","no"],
    "marital status":["single","married","single","marries","divorced","married","divorced","single","married","single"],
    "taxable income":["125k","100k","70k","120k","95k","60k","220k","85k","75k","90k"],
    "cheat":["no","no","no","no","yes","no","no","yes","no","yes"]}
df=pd.DataFrame(dict1)

print(df)


#2ques
print(df.iloc[[0,4,7,8]])

#3.1
print(df.iloc[3:8])

#3.2
print(df.iloc[4:9,2:4])

#3.3
print(df.iloc[:,1:4])
