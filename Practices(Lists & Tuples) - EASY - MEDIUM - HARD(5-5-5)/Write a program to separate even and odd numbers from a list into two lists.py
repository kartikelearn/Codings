#Write a program to separate even and odd numbers from a list into two lists.
l=[int(x) for x in input("Enter: ").split(",")]  # if we don't want .split(",") then we don't need to write spaces or comma in input.
even=[]
odd=[]
for el in l:
    if(el%2==0):
        even.append(el)
    else:
        odd.append(el)
print("Even is: ",even)
print("Odd is: ",odd)