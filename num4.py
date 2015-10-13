import pylab
import numpy as np
import matplotlib as plt

tmin = -20.0
tmax = 20.0
dt = 0.01
tlist = np.arange(tmin, tmax, dt)
pylab.ion()

for i in range (50):
     ylist = [np.cos(2 * t) for t in tlist]
     xlist = [np.sin(t + i) for t in tlist]
     pylab.clf()
     pylab.plot(xlist, ylist)
     pylab.draw()
pylab.close
