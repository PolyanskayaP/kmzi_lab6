import sympy as sy 

ran = sy.primerange(1, 720)
list_x = []
list_y = []

for i, p in enumerate(ran) :
    print(i+1, p)
    list_x.append(p)
    list_y.append(i+1)

import matplotlib.pyplot as plt
import numpy as np

# plot
fig, ax = plt.subplots()

ax.plot(list_x, list_y, linewidth=2.0)
#ax.scatter(list_x, list_y, color = 'orange')

#x.set(xticks=list_x, yticks=list_y)
list_x_EE = [2, 29, 59, 103, 151, 197, 241, 277, 311, 373, 397, 461, 499, 521, 569, 617, 661, 701]
list_y_EE = list_y.copy()
for y in list_y:
    if (y!=1) and not(y % 3 == 0):
        list_y_EE.remove(y)
ax.set(xticks=list_x_EE, yticks=list_y_EE)

ax.set_xlabel('Простые  числа')
ax.set_ylabel('')

for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
    item.set_fontsize(5)
    
plt.axvline(x = 500, color = 'b')
plt.axvline(x = 700, color = 'b')

plt.show()