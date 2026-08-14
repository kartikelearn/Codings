#WAP to find the sum of first n numbers. (using while)
i=1
sum=0
n=int(input("Enter the range: "))
while(i<=n):
    sum=sum+i
    i+=1
print("The sum of 1st n numbers is: ",sum)