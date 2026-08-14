#Write a program that takes 3 numbers as input and prints the largest number.
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
num3=int(input("Enter Number 3: "))
list=[num1,num2,num3]
list.sort()
print("The largest among these three is: ",list[len(list)-1])
print("The largest among these three is: ",max(list))
