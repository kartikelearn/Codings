#Write a program to count how many times a number appears in a list.
l=[1,2,3,1,4,1,6]
word=1
c=l.count(1) # counts
print(c)
print(l.index(1)) # 1st appearance
# by using for element in list
count=0
for el in l:
    if(el==word):
        count+=1
print(count)

#by using a simple for
x=0
for i in range(len(l)):
    if(l[i]==word):
        x+=1
print(x)

# by using while
y=0
i=0
while(i<len(l)):
    if(l[i]==word):
        y+=1
    i+=1
print(y)