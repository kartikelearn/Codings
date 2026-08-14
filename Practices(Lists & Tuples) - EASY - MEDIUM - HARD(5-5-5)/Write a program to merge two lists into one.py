#Write a program to merge two lists into one.
l1=[1,2,3,4,5]
l2=[9,7,6,5,4]
print(l1+l2)
#or
lunion=l1.copy()
for el in l2:
    lunion.append(el)
print(lunion)
# or
lunited=l1.copy()
lunited.extend(l2)
print(lunited)
#or
l1=set(l1)
l2=set(l2)
print(l1.union(l2)) # but this removes duplicates

