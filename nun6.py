import numpy as np
import matplotlib.pyplot as plt

inputing = open ('input.txt', 'r')
data = inputing.read()
data = data.split()
sub = list (map (len, data))
final = max (sub)
objects = range (final)
y_pos = np.arange(len(objects))
performanse = [sub.count(i) for i in objects]


plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Value')
plt.title('Bar title')

plt.show()
