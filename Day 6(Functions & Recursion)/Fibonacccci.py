# Fibbonacci using recursion
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)


def print_fibonacci(nth_term, current=0):
    if current > nth_term-1:
        return
    print(fibonacci(current), end=" ")
    print_fibonacci(nth_term, current + 1)


nth_term=int(input("Enter the nth term: "))
print_fibonacci(nth_term)