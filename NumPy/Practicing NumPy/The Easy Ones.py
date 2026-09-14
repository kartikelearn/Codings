import numpy as np
print(np.__version__)
print(np.__dict__)
print(np.show_config)

# Null Vector of Size 10
null_vector=np.zeros(10,dtype=int)
print(null_vector)
# a=np.linspace(1,10,10,dtype=int)
# print(a)
# print(null_vector.size)
# print(null_vector.itemsize)
print(null_vector.size*null_vector.itemsize)
print(null_vector.__sizeof__())

# print(np.add.__doc__)
print(np.info(np.add))

nulls=np.zeros(10,dtype=int)
nulls[4]=1
print(nulls)

im_arange=np.arange(10,50,dtype=int)
print(im_arange)

print(im_arange[::-1])
print(np.flip(im_arange))

a=np.arange(0,9).reshape((3,3))
print(a)

a=np.array([1,2,0,0,4,0])
print(a[a>0])
indices=(np.where(a!=0))
print(indices)