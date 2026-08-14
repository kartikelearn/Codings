# * * * *
# - * * *
# - - * *
# - - - *
row=1
while row<=4:
    column=1
    while column<=4:
        if(column<=row-1):
            print("-",end=" ")
        else:
            print("*",end=" ")
        column+=1
    print()
    row+=1

# 1
# 2 1
# 3 2 1
# 4 3 2 1
row=1
while row<=4:
    column=1
    while column<=4:
        if(row+1-column>0):
            print(row+1-column,end=" ")
        column+=1
    print()
    row+=1

# #orrr

# 1
# 2 3
# 3 4 5
# 4 5 6 7
row=1
while row<=4:
    column=1
    while column<=4:
        if(column<=row):
            print(row+column-1,end=" ")
        column+=1
    print()
    row+=1

