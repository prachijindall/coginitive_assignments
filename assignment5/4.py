import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100)
print(x)

#4.1
y=x**2

plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('y=x^2')
plt.grid(True)
plt.show()

#4.2
y1=np.sin(x)
plt.plot(x,y1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('y=sin(x)')
plt.grid(True)
plt.show()

#4.3
y2=np.exp(x)
plt.plot(x,y2)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('y=e^x')
plt.grid(True)
plt.show()

#4.4
y3=np.log(np.abs(x)+1)
plt.plot(x,y3)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('y=log(|x|+1)')
plt.grid(True)
plt.show()