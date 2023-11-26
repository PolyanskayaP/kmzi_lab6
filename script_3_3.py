import numpy as np
''''''
list_x = np.arange(1, 90)
#print(list_x)
for p in list_x:
    #print(p, ((3**p) - 3) % p)
    if ((3**p-3)%p == 0)  :#and ((5**p - 5) % p == 0): #and ((7**p - 7) % p == 0) and ((11**p - 11) % p == 0):
       print(p)
       pass
''''''

#print((3**23-3)%23)