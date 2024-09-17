import numpy as np

# creating the array
a = np.array([2, 3, 4])
print(a)

# returns the data type of the items in the array
print(a.dtype)

# creating another array
b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype)

# a common error
# c = np.array(1, 2, 3, 4) # this is not allowed
# print(c)

# this sequence of sequences is turned into a two d array
c = np.array([(1.5, 2, 3), (4, 5, 6)])
print(c)

# a three sequence array is turned into a three dimensional array
a3sequence = np.array([(1, 2, 3), (1, 2, 3), (1, 2, 3)])
print(a3sequence)



