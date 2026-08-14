#Write a recursive function to calculate factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
x=fact(5)
print(x)