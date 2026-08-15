n, m = map(int, input().split())
H=0
l=[]
for i in range(n):
    l.append(int(input()))
A=set()
for j in range(m):
    A.add(int(input()))
B=set()
for k in range(m):
    B.add(int(input()))
for a in A:
    if a in l:
        H+=1
for b in B:
    if b in l:
        H-=1
print(H)