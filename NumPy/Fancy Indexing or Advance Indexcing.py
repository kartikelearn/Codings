# so basically in a simple array we do indexing like
#1D
import numpy as np
a=np.linspace(3,18,6, dtype=int)
# print(a)
# [ 3  6  9 12 15 18]
print(a[0]) # if we wanted to access a element then we would have done this
print(a[[1,0,0,4,3]]) # we can access multiple elements at once

# 2D
a.resize(3,4)
# print(a)
# [[ 3  6  9 12]
#  [15 18  0  0]
#  [ 0  0  0  0]]
print(a[1:,])  # The way we were doing
print(a[[1,2]]) # we can directly access row 1 and 2
print(a[[0,1,2],[3,2,1]]) # if we want to access (0,3) (1,2) and (2,1) elements

# we can use take() instead of the above it becomes quite useful when we deal with multidimentional data and play with axes
# like see this
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.take(a,[1,2],axis=0)) # returns the columns and for axis 1 returns the rows
print(np.take(a,[0,1,2])) # it will work like print(a[[0,1,2]])

# We have also a method named put() we can use this as opposite of take it means we can put data at specific indices using put
np.put(a,[1,2,3],[100,200,300])
print(a)

rg=np.random.default_rng()
a=rg.integers(0,100,size=50)
print(a)
print(a[a%2==0]) # so we can basically filter any data like this it's called boolean Indexing ---> keep the elements if the conditions are true

print(a[(a>50)&(a%2==0)]) # so we can also use &,| and ~ (or, not and) as like multiple conditions
# We can use the where() to check the index of the element where the condition matches
print(np.where(a>50)) # gives the index where this condition happens

# It's very useful like see
marks=np.array([60,10,40,30,81])
print(np.where(marks>=30,"Pass", "Fail")) # it's useful to do filtering

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(np.argwhere(a>50)) # it's quite useful in multidimentional arrays as it gives the co-ordinates like (row,columns)


# To solve system of linear equations:
A = np.array([
    [24, 1],
    [23, -1]
])

B = np.array([5, 1])
x=np.linalg.solve(A,B).astype(int)
print(x)