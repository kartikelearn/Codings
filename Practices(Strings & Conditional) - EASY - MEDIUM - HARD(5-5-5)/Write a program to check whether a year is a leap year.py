#Write a program to check whether a year is a leap year.
year=int(input("Enter Your Year: "))
if(year%400==0):
    print("Leap Year")
elif(year%100!=0 and year%4==0):
    print("Leap Year")
else:
    print("Not a leap Year")
         