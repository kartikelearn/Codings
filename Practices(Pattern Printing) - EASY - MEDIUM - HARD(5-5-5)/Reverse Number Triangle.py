# Reverse Number Triangle
# 1
# 2 1
# 3 2 1
# 4 3 2 1
row=1
num=1
while(row<=4):
    column=1
    while(column<=4):
        if(column<=row):
            print(column,end=" ")
        column+=1
    print()
    row+=1
