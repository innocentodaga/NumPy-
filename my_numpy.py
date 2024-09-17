import numpy as np
#numpy is a library used for scientific computing applications and is ancronym
# for "Numerical python"
# main categories of numpy are: fourier transform and shape manipulaton,
# mathematical and logical operations and linear algebra and random number generation

# arrays:- the central feature of numpy is the array object class
# Arrays are similar to lists in python except that every element of an array must be of the same datatype
a = np.array([1, 4, 5, 8], float)
print(a)
print(type(a))

# accessing the 4th values of the array
print(a[3])

# modifying the values in the array
a[0] = 5
print(a)

# slicing an array:- prints the first 2 elements in the array list
print(a[:2])







#adding a 2 to each element in the list array.
nums = np.array([2, 3, 4, 5, 6])
nums2 = nums + 2
print(nums2)




