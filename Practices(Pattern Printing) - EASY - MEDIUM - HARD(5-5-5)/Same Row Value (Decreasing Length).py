#Same Row Value (Decreasing Length)
# 1 1 1 1
# 2 2 2
# 3 3
# 4
row=1
while(row<=4):
    column=1
    while(column<=4):
        if(column>=row):
            print(row,end=" ")
        column+=1
    print()
    row+=1