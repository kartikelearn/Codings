list=[]
list.append(input("Enter the Element 1 of your list "))
list.append(input("Enter the Element 2 of your list "))
list.append(input("Enter the Element 3 of your list "))
list.append(input("Enter the Element 4 of your list "))
list.append(input("Enter the Element 5 of your list "))
listcopied=list.copy()
listcopied.reverse()
if(list==listcopied):
    print("Palindrome")
else:
    print("Not Palindrome")