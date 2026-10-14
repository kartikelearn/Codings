#Print 1-N using a Tail recursion
def one_to_n(N):
    if N<=-1:
        return
    one_to_n(N-1)
    print(N)
N=int(input("Enter the Last No... "))
i=int(input("Enter the starting num..."))
one_to_n(N)