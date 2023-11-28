import math
import numpy
x_li = [1009,  1013,  1019,  1021,  1031,  1033,  1039,  1049,  1051,  1061,  1063,
  1069,  1087,  1091,  1093,  1097,  1103,  1109,  1117,  1123,  1129,  1151,  1153,
  1163,  1171,  1181,  1187,  1193,  1201,  1213,  1217,  1223,  1229,  1231,  1237,
  1249,  1259 , 1277,  1279,  1283,  1289,  1291,  1297 ]

n_ler = [10, 15, 20, 30, 35]
sr_n_ler = []
for n in n_ler:
    sum = 0
    for ch in x_li[:n]:
        sum += ch
    sr = sum / n 
    sr_n_ler.append(sr)
    #print(sr)
sr_n_logar = 1/numpy.log(sr_n_ler)

logarifm_x = []
for ch in x_li:
    logarifm_x.append(1/math.log(ch))
    
#print(sr_n_ler)
#print(logarifm_x)

for n, n_sr in zip(n_ler, sr_n_logar):
    print(n)
    for ch_log, x in zip(logarifm_x[:n], x_li[:n]):
        print("простое число = ", x,": abs(", n_sr, "-", ch_log, ") =", abs(n_sr-ch_log))