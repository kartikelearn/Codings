#Right Angle Inverted
# - * * * * 
# - - * * * 
# - - - * *
# - - - - *
row=1
while(row<5):
    column=1
    while(column<=5):
        if(column<=row):
            print("-",end=" ")
        else:
            print("*",end=" ")
        column+=1
    print()
    row+=1