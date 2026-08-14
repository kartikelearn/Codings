#Write a program to find the sum of all elements in a list.
l=[1,2,3,4,5]
print(sum(l)) # in build
sum=0
for i in range(len(l)):
    sum=l[i]+sum

print(sum)