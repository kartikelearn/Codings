#Write a program to take a 3-digit number and print the sum of its digits.
number=int(input("Enter a 3 digit number: "))
print("The addition of the digits of ",number,"is: ",(number//100)+((number%100)//10)+((number%100)%10))