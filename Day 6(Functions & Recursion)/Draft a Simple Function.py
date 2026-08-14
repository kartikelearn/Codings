# Functions are block of statements that performs a Task
def sum(a,b):  #definiton function_name(par1,par2...par.nth):
    s=a+b       # some work
    return s        # return var
num1=int(input("Enter the No.. : "))
num2=int(input("Enter the No.. : "))
print(sum(num1,num2))  # function call ---> function(arg1,arg2...)

print("Kartike",end="loves")
print("Nothing")
print("Kartike","Loves","Nothing",sep="%")