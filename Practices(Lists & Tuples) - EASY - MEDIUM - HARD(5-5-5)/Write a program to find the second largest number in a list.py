#Write a program to find the second largest number in a list.
l=[4,3,2,4,5]
lcopied=l.copy()
lcopied.remove(max(lcopied))
print(max(lcopied))

#or

greatest=l[0]
for el in l:
    if(el>greatest):
        greatest=el
print(el)
# Then remove the greatest from list and print it.

#or

l = [6, 4, 3, 2, 5]

largest = l[0]
second = l[0]

for el in l:
    if el > largest:
        second = largest
        largest = el
    elif el > second and el != largest:
        second = el

print(second)