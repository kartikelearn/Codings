#Write a program to convert seconds into hours, minutes, and seconds.
sec=float(input("Enter seconds here: "))
print(sec//(60*60),"hrs",(sec%(60*60))//60,"mins",sec%60,"secs")

# // this operator is call floor division ( it return the value with no decimal points)

