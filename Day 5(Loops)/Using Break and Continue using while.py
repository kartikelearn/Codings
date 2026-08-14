i=1
while(i<=5):
    print(i)
    i+=1
    if(i==3):
        break

j=1
while(j<=5):
    if(j==3):
        j+=1
        continue # skip current iteration
    print(j)
    j+=1