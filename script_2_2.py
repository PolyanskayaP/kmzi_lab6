all_prost_2_2 = [1009,  1013,  1019,  1021,  1031,  1033,  1039,  1049,  1051,  1061,  1063,
  1069,  1087,  1091,  1093,  1097,  1103,  1109,  1117,  1123,  1129,  1151,  1153,
  1163,  1171,  1181,  1187,  1193,  1201,  1213,  1217,  1223,  1229,  1231,  1237,
  1249,  1259 , 1277,  1279,  1283,  1289,  1291,  1297 ]

L_i_2_2 = []
for i in range(len(all_prost_2_2)-1):
    li = all_prost_2_2[i+1] - all_prost_2_2[i]
    L_i_2_2.append(li)
    
print(L_i_2_2)
import statistics
print("среднее: ",statistics.mean(L_i_2_2))

import matplotlib.pyplot as plt
import numpy as np
#plt.style.use('_mpl-gallery')

# make data:
x = np.arange(len(L_i_2_2))
y = L_i_2_2

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

#ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
