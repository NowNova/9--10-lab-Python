import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

degrees = range(1, 8)
fig, ax = plt.subplots()
for degree in degrees:
    x = np.linspace(-1, 1, 1000)
    y = legendre(degree)(x)
    ax.plot(x, y, label=f'n = {degree}')

ax.set_title('Полиномы Лежандра')
ax.legend()
plt.show()

# from scipy.special import eval_legendre

# x = np.linspace(-1, 1, 1000)
# degrees = [1, 2, 3, 4, 5, 6, 7]

# plt.figure()
# plt.title('Полиномы Лежандра')

# for degree in degrees:
#     y = eval_legendre(degree, x)
#     plt.plot(x, y, label='n = {}'.format(degree))

# plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1))
# plt.show()