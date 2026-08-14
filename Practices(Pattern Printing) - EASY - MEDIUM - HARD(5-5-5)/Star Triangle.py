# *
# * *
# * * *
# * * * *
row=1
while(row<=4):
    column=1
    while(column<=4):
        if(column>=row):
            print(5-column,end=" ")
        # else:
        #     print(" ",end=" ")
        column=column+1
    print()
    row=row+1