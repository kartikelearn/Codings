#Indexing, Slicing & Iterating through any Array
import numpy as np
a=np.arange(1,16,2)*3
print(a)
print(a[:6:2])  # Start:Stop:Step
a[:6:2]=5
print(a)

#2D
# [[ 5  9  5 21]
#  [ 5 33 39 45]]

a=a.reshape(2,4)
print(a)
print(a[0,1]) #one element
print(a[0:2,1]) # a column
print(a[0]) # to take the 1st line one(it's something like axis=0) 
print(a[1]) # 2nd line
# a=a.reshape(2,2,2)
# print(a)
b=np.array(
[[ 0, 1, 2, 3],
[10, 11, 12, 13],
[20, 21, 22, 23],
[30, 31, 32, 33],
[40, 41, 42, 43]])

print(np.shape(b))
a=b.reshape(2,5,2)
# [[ 0  1]
#   [ 2  3]
#   [10 11]
#   [12 13]
#   [20 21]]

#  [[22 23]
#   [30 31]
#   [32 33]
#   [40 41]
#   [42 43]]]

print(a[0,0],a[1,0]) # for a row in a 3D
# print(a)
print(a[1,...],end="\n\n\n")
print(a[0,:,:],end="\n\n\n") # for taking any row out
print(a[:,:,1],end="\n\n\n") # for taking any column out

for row in a:
    print(row)


for element in a.flat:  # we can access elements using this
    print(element)