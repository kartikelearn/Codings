s1=int(input("Enter the marks of Subject 1 "))
s2=int(input("Enter the marks of Subject 2 "))
s3=int(input("Enter the marks of Subject 3 "))
s4=int(input("Enter the marks of Subject 4 "))
s5=int(input("Enter the marks of Subject 5 "))
tmarks=(s1+s2+s3+s4+s5)/5
if(tmarks>=35):
    if(tmarks>=80):
        print("A+")
    elif(tmarks>=60):
        print("A")
    elif(tmarks>=45):
        print("B")
    else:
        print("C")
else:
    print("Fail")
