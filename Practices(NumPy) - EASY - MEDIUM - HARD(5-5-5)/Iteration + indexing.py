import numpy as np
a = np.arange(1, 31).reshape(5, 6)
# [[ 1  2  3  4  5  6]
#  [ 7  8  9 10 11 12]
#  [13 14 15 16 17 18]
#  [19 20 21 22 23 24]
#  [25 26 27 28 29 30]]
#Don't use flat
# 1 6
# 7 12
# 13 18
# 19 24
# 25 30
# print(a)
for el in a:
    print(el[0],el[-1])
