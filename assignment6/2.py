import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dict1={ 'subjects':['hindi','pbi','eng','sci','maths'],
       'marks':[89,98,66,77,87]}
df=pd.DataFrame(dict1)
print(df)

sns.barplot(x="subjects",y="marks",data=df,palette='viridis')

for i, marks in enumerate(df["marks"]):
    plt.text(i, marks + 1, str(marks), ha='center', fontsize=10)
plt.xlabel('subjects')
plt.ylabel('marks')
plt.title('subjects marks')
plt.grid()
plt.show()