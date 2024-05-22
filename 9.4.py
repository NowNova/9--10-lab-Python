import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
maxi = 0
for i in range(len(x)-1):
    if x[i] == 0 and maxi < x[i+1]:
        maxi = x[i+1]
print(maxi)