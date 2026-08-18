import numpy as np
a = np.arange(60).reshape(3, 4, 5)
# print(a)
# (3, 4, 2)
# [[[ 0  1  2  3  4]
#   [ 5  6  7  8  9]
#   [10 11 12 13 14]
#   [15 16 17 18 19]]

#  [[20 21 22 23 24]
#   [25 26 27 28 29]
#   [30 31 32 33 34]
#   [35 36 37 38 39]]

#  [[40 41 42 43 44]
#   [45 46 47 48 49]
#   [50 51 52 53 54]
#   [55 56 57 58 59]]]
#Without using a loop, extract the last two columns from every row of every layer.
a=a[::,::,3::]
print(np.shape(a))