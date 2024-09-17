import numpy as np

# creating the array and specifying the datatype
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

# creating an an array with zeros
# the default type of an array is float
zero = np.zeros((3, 4))
print(zero)

# Creating array of ones
# the 2 represents two arrays to be created
# the 3 represents the dimension of the array or the axes of the array
# the 4 represents the length of the items or axes
ones = np.ones((2, 3, 4),dtype=np.int16)
print(ones)
