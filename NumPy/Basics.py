# Starting NumPy
import numpy as np
a=np.array([1,2,3,4], dtype='int32') # we can also change the dtype using dtype='datatype'
print(type(a))
print(a)
print(a.ndim) # Returns the dimension of Array.(1,2..)
print(a.shape) # Returns the shape of Numpy Array.(n,m)
print(a.size) # Returns the no.. of elements in the array,(n*m)
print(a.dtype) # Returns the type of data of each element.
print(a.itemsize) # Returns the size of each element in the array.
print(a.dtype.itemsize) # Equivalent to itemsize
print(a.data) # Returns the memory location
print(a[0],a[1]) # Accessing the element

# Two Useful functions
b=np.arange(6)
print(b.shape)
print(b)
b=b.reshape(2,3) # Check the no.. of elements whenever you reshape the array
print(b)