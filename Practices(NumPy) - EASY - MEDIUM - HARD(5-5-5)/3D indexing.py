# [
#     [
#         [ 0,  1,  2,  3],
#         [ 4,  5,  6,  7]
#     ],
#     [
#         [ 8,  9, 10, 11],
#         [12, 13, 14, 15]
#     ]
# ]

# create this using using np.arange() and reshape() and then extract the last row or [12 13 14 15]
import numpy as np
a=np.arange(16).reshape(2,2,4).astype(int)
print(a)
print(a[1,1])

#extract this from same 3D array
# [
#     [4 5 6 7],
#     [12 13 14 15]
# ]
#using a single slicing expression.
print(a[0:2,1])