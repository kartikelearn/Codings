# * * * -
# * * - -
# * - - -
row = 1

while row < 4:
    column = 1
    while column <= 4:
        if column <= 4 - row:
            print("*", end=" ")
        else:
            print("-", end=" ")
        column += 1
    print()
    row += 1