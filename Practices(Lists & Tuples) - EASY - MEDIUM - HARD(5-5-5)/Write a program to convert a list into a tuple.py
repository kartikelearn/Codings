#Write a program to convert a list into a tuple.
l=[1,2,3,4,5]
l=tuple(l)
print(l)
t=[]
#use for or while and append all elements of this list into a null tuple.
for el in l:
    t.append(el)
print(tuple(t))