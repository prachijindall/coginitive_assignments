import numpy as np
import matplotlib.pyplot as plt
m=float(input('enter the value'))
x=np.linspace(-10,10,100)
y1=m*x**2
y2=m*np.sin(x)
plt.plot(x,y1,label='y=m*x^2')
plt.plot(x,y2,label='y=m*sin(x)')
plt.legend()
plt.grid()
plt.title('function')
plt.show()