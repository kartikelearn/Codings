#Write a program to check whether a string is palindrome.
str=str(input("Enter Your String here: "))
str=list(str)
strcopied=str.copy()
strcopied.reverse()
if(str==strcopied):
    print("Palindrome")
else:
    print("Not Palindrome")