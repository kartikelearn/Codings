# Recursion is a function which calls itself
def show(n):
# show 5,4,3,2,1
    if(0<=n):  # base case
        print(n)
        show(n-1)
show(5)