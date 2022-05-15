import matplotlib.pyplot as plt
import numpy as np


# 3x+1
def hail(x):
    """Takes in an integer and returns a list of the Collatz bounces."""
    bounces = []
    while x > 1:
        while x % 2 != 0:
            x = (x * 3) + 1
            bounces.append(int(x))
            # print(x)
        while x % 2 == 0:
            x /= 2
            # print(x)
            bounces.append(int(x))
    return bounces




twenty_seven = np.array(hail(27))
twenty_eight = np.array(hail(28))
i = np.array(hail(432))
print(twenty_seven)
print('-'*20)
print(twenty_eight)
print('-'*20)
print(i)

plt.plot(twenty_seven)
plt.plot(twenty_eight)
plt.plot(i)
plt.grid(alpha=0.4)
plt.show()
