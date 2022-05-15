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

def collatz(lst):
    """Takes in a list of integers and returns a dictionary with the number of bounces for each item in the list"""
    master = {}
    for item in lst:
        master[item] = hail(item)
    return master


# twenty_seven = np.array(hail(27))
# twenty_eight = np.array(hail(28))
# i = np.array(hail(432))
# print(twenty_seven)
# print('-'*20)
# print(twenty_eight)
# print('-'*20)
# print(i)
#
# plt.plot(twenty_seven)
# plt.plot(twenty_eight)
# plt.plot(i)
# plt.grid(alpha=0.4)
# plt.show()

nums = np.arange(10, 201)

d = collatz(nums)
print(d)
print('-'*30)
print(len(d[27]))
print(len(d[28]))
print(len(d[29]))
print(len(d[30]))
print(len(d[31]))

plt.plot(d[27])
plt.plot(d[31])
plt.show()

# We need to get the number of bounces per int and for hail
# we need to change bounces to a better descriptor