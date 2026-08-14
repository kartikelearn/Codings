#Same Number Triangle
# 1
# 2 2
# 3 3 3
# 4 4 4 4
row=1
while(row<=4):
    column=1
    while(column<=row):
        print(row,end=" ")
        column+=1
    print()
    row+=1