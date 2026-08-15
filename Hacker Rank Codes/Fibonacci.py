first=0
second=1
n=int(input("Enter nth term: "))
if(first==0 and second==1):
    print(first,"\t",second,end="\t")
i=0
while i<=n:
    third=first+second
    first=second
    second=third
    print(third,end="\t")
    i+=1