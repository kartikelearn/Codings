import numpy as np
a = np.arange(24).reshape(4, 6)
for element in a.flat:
    if element%3==0:
        print(element)