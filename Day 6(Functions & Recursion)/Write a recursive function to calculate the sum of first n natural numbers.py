#Write a recursive function to calculate the sum of first n natural numbers. 
def addition(n=int(input("Enter the nth terms: "))):
    if(n==0):
        return 0
    else:
        return n+addition(n-1)
print(addition())