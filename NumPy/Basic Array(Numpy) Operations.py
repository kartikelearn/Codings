#Basic Array Operations
import numpy as np
a=np.linspace(1,10,5,dtype='int')
print(a) 
b=np.array([3,4,5,2,8])
c=a+b # Addition in a matrix
print(c)
d=a*b # element wise product
# same we can do difference
a=np.append(a,4)
a=a.reshape(2,3)
b=np.append(b,5)
b=b.reshape(3,2)
#Here we have some methods or functions to do matrix multiplication (2,3)*(3,2)

c=a@b # Matrix Multiplication using @ operator
print(c)
c=a.dot(b) # using dot method
print(c) 

# we can use +=, or *= to just modify the already made arrays without creating new one

a=np.ones((2,3),dtype='int32')
rg=np.random.default_rng(1)
a*=3
print(a)
b=rg.random((2,3))
c=a+b  # it can succeed but if i do something like a+=b so it will fail due to the casting or same type error float64 + int32 can't happen it means that we can't change a int32 to float64
print(c)

d=np.exp(c*1j)
print(d)

# We can also do sum, min and max of an array e.g.,
a=np.array([1,2,3,8,1])
print(a.sum())
print(np.add(c,d))
print(a.min())
print(a.max())
a.sort()
print(a)

#Deep copy and shallow copy
# in numpy if we do something like a=b then it would be a shallow copy but if we do like a=np.copy(b) then it would be a deep copy
# but if we do the same thing in lists like a=b or a=b.copy() will make the shallow copy, it doesn't create a new one array

# axis 0 is column and axis 1 is row.

n=np.arange(12).reshape(3,4).astype(int)
print(n)
b=n.cumsum(axis=0)
print(b)