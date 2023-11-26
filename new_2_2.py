import sympy as sy 
import numpy as np
import matplotlib.pyplot as plt

ran = sy.primerange(2, 30)
r_list = []

for r in ran:
    r_list.append(r)

#x_li = [x   for x in r_list] 

x_li = [1009,  1013,  1019,  1021,  1031,  1033,  1039,  1049,  1051,  1061,  1063,
  1069,  1087,  1091,  1093,  1097,  1103,  1109,  1117,  1123,  1129,  1151,  1153,
  1163,  1171,  1181,  1187,  1193,  1201,  1213,  1217,  1223,  1229,  1231,  1237,
  1249,  1259 , 1277,  1279,  1283,  1289,  1291,  1297 ]
L = []
r_list = x_li

for i in range(len(r_list)-1):
    L.append(r_list[i+1] - r_list[i])
    print(x_li[i], r_list[i+1] - r_list[i])

print(x_li, L)
popx = x_li.pop()

x_li2 = [x + y/2  for x,y in zip(r_list, L)] #+0.5

x = x_li2
y = L
fig, ax = plt.subplots()

x_li.append(popx)
#ax.set(xticks=x_li, yticks=y, rotation= 90)
plt.xticks (x_li, rotation= 90 )
plt.yticks (y)
plt.bar(x, y, linewidth=1.0, edgecolor='k', width=y)
plt.show()