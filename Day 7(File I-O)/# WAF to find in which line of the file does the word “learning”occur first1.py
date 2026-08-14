# WAF to find in which line of the file does the word “learning”occur first. 
# Print -1 if word not found. 
# From a file containing numbers separated by comma, print the count of even numbers.
word="learning"
data=True
i=1
with open("find.txt","r") as f:
    while(data):
        data=f.readline()
        if(word in data):
            print(i)
        else:
            print("-1")
        i+=1
        


