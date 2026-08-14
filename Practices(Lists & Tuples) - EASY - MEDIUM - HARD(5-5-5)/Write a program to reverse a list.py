#Write a program to reverse a list.
l=[1,2,3,4,5]
l.reverse()
print(l)
# by for
y=[]
for j in range(len(l)-1,-1,-1):
    y.append(l[j])
print(y)
# by while
x=[]
i=len(l)-1
while(i>=0):
    x.append((l[i]))
    i-=1
print(x)

# most important(used in string)
lst = [1, 2, 3, 4, 5]
rev = lst[::-1]
print(rev)

# by using for el in list
lst = [1, 2, 3, 4, 5]
rev = []

for el in lst:
    rev = [el] + rev

print(rev)