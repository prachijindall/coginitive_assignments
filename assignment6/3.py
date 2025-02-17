import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
roll=12345
np.random.seed(roll)
data=np.random.randn(50)
cum_sum=np.cumsum(data)
fig,axs=plt.subplots(2,2)
axs[0,0].plot(cum_sum,color='red')
axs[0,0].set_title('line plot')
axs[0,0].grid()

axs[0,0].scatter(range(50),data,color='red')
axs[0,0].set_title('scatter plot')
axs[0,0].grid()

plt.show()