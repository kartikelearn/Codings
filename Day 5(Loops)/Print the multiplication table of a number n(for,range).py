# Print the multiplication table of a number n.
n=int(input("Enter Number of Table: "))
for i in range(1,11,1):
    print(n,"*",i,"is",n*i)