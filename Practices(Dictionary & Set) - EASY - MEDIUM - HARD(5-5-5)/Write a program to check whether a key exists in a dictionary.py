#Write a program to check whether a key exists in a dictionary.
count=0
dict={
    "Sex":"Male",
    "Orgasum":"G-Spot",
    "Body-Count":29
}
x="Sex"
list=list(dict)
if(list.index(x)!=-1):
    print("It Exists")
else:
    print("It doesn't Exist")
#or
if dict.get(x) is not None:
    print("It Exists")
else:
    print("It doesn't Exist")