# Functional Recursion, Sum of N natural numbers
def sum_of_n(N):
    if N==1:
        return 1
    return N+sum_of_n(N-1)
num=int(input("Enter the numbers: "))
print(sum_of_n(num))