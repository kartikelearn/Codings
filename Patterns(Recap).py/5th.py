# 1
# 2 3
# 4 5 6
# 7 8 9 10

row=1
num=1
while(row<=4):
    column=1
    while(column<=row):
        print(num,end=" ")
        num+=1
        column+=1
    print()
    row+=1
