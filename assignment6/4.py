import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://github.com/AnjulaMehto/MCA/raw/main/company_sales_data.csv"
data = pd.read_csv(url)
total_profit = data['total_profit']
plt.figure(figsize=(10, 6))
sns.lineplot(x=data['month_number'], y=total_profit, marker='o', color='blue')
plt.title('Total Profit of All Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()
total_profit = data['total_profit']
plt.figure(figsize=(10, 6))
sns.lineplot(x=data['month_number'], y=total_profit, marker='o', color='blue')
plt.title('Total Profit of All Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.grid(True)
plt.show()
data.set_index('month_number').plot(kind='bar', figsize=(15, 10))
plt.title('Bar Chart of All Features/Attributes')
plt.xlabel('Month')
plt.ylabel('Values')
plt.grid(True)
plt.legend(title='Features')
plt.show()

