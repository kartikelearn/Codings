#Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
i=0
x=int(input("Enter the number you want to check: "))
list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for i in range(i,len(list),1):
    if(list[i]==x):
        print("The element find at index: ",i)
    else:
        print("Loading..")
    i+=1