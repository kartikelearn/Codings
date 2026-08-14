import numpy as np


# 1D - A sequence of elements simple array(looks like list)
a=np.array([1,2,3,4,5])
print(a.ndim)

# 2D - Sequence of Sequences(Collection of 1D arrars or List in list)
b=np.array([[1,2,3,4],[6,4,2,4]])
print(b.ndim)

# 3D - Sequence of Sequences of Sequences(Collection of 2D arrays or list in lists in lists)
c=np.array([[[1,2,3,4],[4,5,6,7]],[[1,2,3,4],[8,7,6,5]]])
print(c.ndim)

##### Some important Functions
d=np.arange(10,30,2).reshape(2,5) # Syntax includes arange(start,stop,step) same like loops
print(d)

e=np.linspace(10,30,10,dtype=int).reshape(5,2) # Syntax contains linspace(start,stop,size) here size (- to n(el) or n*m
print(e)
# OR
# e=np.round(np.linspace(10,30,10)).astype(int).reshape(5,2)
# print(e)
# OR
# e=np.linspace(10,30,10).reshape(5,2).astype('int32')
# print(e)

a=np.zeros((3,4,5)) # 3 blocks, 4 rows in 3 blocks & 5 columns in 4 rows.. (blocks,rows,columns)
print(a)

b=np.identity(3)
print(b)

c=np.ones((2,3))
print(c)

d=np.empty((4,5))
print(d)

e=np.ones_like(a)  # Same goes for empty_like and zeros_like
print(e)

a=np.random.rand(2,3)   # uniform [0,1)
print(a)

a=np.random.randn(2,2)  # normal distribution
print(a)

a=np.random.randint(1,10,(2,3))  # random ints  Syntax - randint(start,stop,shape)
print(a)

def f(i,j): return i+j # it basically creates 2 arrays i(rows) and j(columns) 
a=np.fromfunction(f, (3,3), dtype=int) # 0+0=1, 0+1=2...like this row+column
print(a)

a=np.fromfile("nums.txt",sep=",",dtype=int).reshape(2,7) # np.loadtxt can work,sep=delimiter
print(a)


# By Default the data of created array is Float...