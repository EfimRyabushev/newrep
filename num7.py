import numpy as np
import matplotlib.pyplot as plt


def veershtrass(x):
   acc = 0 
   for i in range(100):
       acc += 0.5 ** i * np.cos(3 ** i * np.pi * x)
   return acc 

x=np.arange(-10,10.01,0.01)
plt.plot(x,veershtrass(x))
plt.show()
