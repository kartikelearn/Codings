#Write a program to check whether a character is alphabet, digit, or special character.
Click=str(input("Click on your keyboard: "))
if(Click>='a'<='z' or Click>='A'<='Z'):
    print("Alphabet")
    if(Click>='a'<='z'):
         print("Lower case")
    else:
         print("Upper case")
elif('0'<=Click<='9'):
    print("Digit")
    if(Click=='0'):
         print("Zero")
    else:
         print("Non-Zero")
else:
    print("Special Character")
