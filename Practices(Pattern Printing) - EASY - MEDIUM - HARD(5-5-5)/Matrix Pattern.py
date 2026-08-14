#1. Matrix Pattern
# 1 2 3
# 4 5 6
# 7 8 9
num = 1
i = 0

while i < 3:          # rows
    j = 0
    while j < 3:      # columns
        print(num,end=" ")
        num += 1
        j += 1
    print()
    i += 1
