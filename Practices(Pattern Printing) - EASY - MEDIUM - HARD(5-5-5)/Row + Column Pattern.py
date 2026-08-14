# Row + Column Pattern
# 1
# 2 3
# 3 4 5
# 4 5 6 7
row=1
while(row<=4):
    column=1
    while(column<=row):
        print(column+row-1,end=" ")
        column+=1
    print()
    row+=1