word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("It Exists.") # searching if the word learning exist
        print(data.index(word)) # searching the word if it exists
    else:
        print("It doesn't exist.")