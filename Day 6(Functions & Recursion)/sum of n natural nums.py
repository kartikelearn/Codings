#Sum of N natural Numbers Using Recursion
def sum_of_n(sum,i,numbers):
    if i>numbers:
        print(sum)
        return
    return sum_of_n(sum+i,i+1,numbers)
i=int(input("Enter the 1st Num: "))
num=int(input("Enter the 2nd Num: "))
sum=0
sum_of_n(sum,i,num)