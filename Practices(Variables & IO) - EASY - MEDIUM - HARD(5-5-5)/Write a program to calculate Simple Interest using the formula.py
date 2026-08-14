#Write a program to calculate Simple Interest using the formula: prt/100
principle=int(input("Enter the amount: "))
rate=float(input("Enter the rate: "))
time=int(input("Time: "))
print("The simple interest is: ",(principle*rate*time)/100)
