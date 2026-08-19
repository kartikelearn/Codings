import numpy as np
rg=np.random.default_rng(1)
a=np.floor(10*rg.random((3,4)))
print(a)
print(a.ravel())
print(a.reshape(4,3))
print(a.T)

# The above all don't make changes in the array, they return the modified array where as
print(a)
a.resize((4,3)) #change the actual size, data can be added/removed
print(a)

print(a.reshape((3,-1))) # if we write a -1 then the other dimension are automatically created


# Stacking there are two methods np.vstack(), np.hstack()
a=np.floor(10*rg.random((2,2)))
print(a)
b=np.floor(10*rg.random((2,2)))
print(b)
print(np.vstack((a,b)))
print(np.hstack((a,b)))
a=np.array([1,2,3])
b=np.array([4,5,6])
from numpy import newaxis
print(np.hstack((a,b)))
print(np.column_stack((a,b))) # It basically stacks a 1D array as column in a 2D array.
print(a[:,newaxis]) # to  ake the array vertical
print(b[:,newaxis])
print(np.column_stack((a[:, newaxis], b[:, newaxis]))) # make it horizontal
print(np.hstack((a[:, newaxis], b[:, newaxis]))) # works same as column_stalk


#In complex cases _r and _c are useful forr creating arrays by stacking numbers along one axis
a=np.r_[1:5,0,8,2]
print(a)

# hsplit(a,3) ---> it will split one array horizontally in three, we can use vsplit(a,3) like this and array_split() along any axis
a=np.floor(10*rg.random((6,6)))
# print(a)
# print(np.hsplit(a,3))
# [[7. 2. 4. 9. 9. 7.]
#  [5. 2. 1. 9. 5. 1.]
#  [6. 7. 6. 9. 0. 5.]
#  [4. 0. 6. 8. 5. 2.]
#  [8. 5. 5. 7. 1. 8.]
#  [6. 7. 1. 8. 1. 0.]]
print(np.hsplit(a,(4,5)))

print(np.repeat(a,3)) #Each element gets repeated
print(np.tile(a,3)) # the whole array or pattern is printed

