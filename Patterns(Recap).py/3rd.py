# * * * *
# * * *
# * *
# *

row=1
while(row<=4):
    column=1
    while(column<=4):
        if(column>=row):
            print("*",end=" ")
        column+=1
    print()
    row+=1

#orrrrr
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

#orrrrrr
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