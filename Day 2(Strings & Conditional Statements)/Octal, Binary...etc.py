i=1
final=int(input("Enter Your Input: "))
n=final
while i<=final:
    print(i,end=" ")
    i+=1

print()

n = int(input("Enter n: "))
for num in range(1, n + 1):
    temp = num
    result = ""

    while temp > 0:
        result = str(temp % 8) + result
        temp = temp // 8

    print(result, end=" ")