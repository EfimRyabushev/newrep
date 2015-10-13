import numpy as np
import matplotlib.pyplot as plt
def function(x):
    expr = 1 + (np.sin(x) ** 2)
    final = 1 / expr
    base = 1 + np.tan(final)
    one = x ** 2 + 1
    two = np.exp(-(abs(x) / 10))
    return np.log(one * two, base)

x=np.arange(-10,10.01,0.01)
plt.plot(x,function(x))
plt.show()
