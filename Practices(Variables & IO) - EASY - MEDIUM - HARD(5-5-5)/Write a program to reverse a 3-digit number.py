#Write a program to reverse a 3-digit number.
number=int(input("Enter the number: "))
print("The reverse of",number,"is:",((number%10)*100)+(((number//10)%10)*10)+(number//100))