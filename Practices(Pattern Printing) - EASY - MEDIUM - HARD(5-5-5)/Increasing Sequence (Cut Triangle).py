# Increasing Sequence (Cut Triangle)
# 1 2 3 4
# 2 3 4
# 3 4
# 4
row=1
while(row<=4):
    column=1
    while(column<=4):
        if(column>=row):
            print(column,end=" ")
        column+=1
    print()
    row+=1
    