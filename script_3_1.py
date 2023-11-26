import matplotlib.pyplot as plt
import numpy as np

x = np.arange(500, 700)
#x = np.arange(1,30)
x_del = np.zeros(len(x))
k_arr = [2,3,5,7,11,13,17,19,23,29]
plt_x = []
plt_y = []

for i in range(1,11):
    for num, xi in enumerate(x): 
        for q in range(i):
            if (xi % k_arr[q] == 0):
                x_del[num] = 0
                break
            else:
                x_del[num] = 1
    plt_x.append(i)
    plt_y.append(sum(x_del)/len(x))    
        
print(plt_x, plt_y)

import matplotlib.pyplot as plt
import numpy as np

# make data
#x = plt_x
x = k_arr
y = plt_y

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=x)

plt.show()