#Write a program to find the smallest element in a list.
l=[1,5,3,6,2]
l.sort()
print(l[0])
# shortcut
print(min(l))
# by for
smallest=l[0]
for el in l:
    if(el<smallest):
        smallest=el
print(smallest)
# using while
smallest=l[0]
i=0
while(i<len(l)):
    if(l[i]<smallest):
        smallest=l[i]
    i+=1
print(smallest)
