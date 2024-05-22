import numpy as np
n = int(input("Введите число элементов вектора: "))
list = []
for i in range(n):
    num = int(input("Введите элемент вектора: "))
    list.append(num)
x = np.array(list)
listnumbers = []
listamount = []
for i in x:
    if i not in listnumbers:
        listnumbers.append(i)
        listamount.append(1)
    else:
        ind = listnumbers.index(i)
        listamount[ind] += 1
print(listnumbers)
print(listamount)