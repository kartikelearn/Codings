#WAF to find the factorial of n. (n is the parameter)
def fact(n=5):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
        i+=1
    print(fac)
fact()
