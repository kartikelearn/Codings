#With syntax
with open("FDemo.txt","r") as f: # automatically closes file
    data=f.read()
    print(data)

with open('FDemo.txt','w') as f:
    f.write("Bhosdiwal")


import os
print(os.getcwd())

with open("newfile.txt", "x") as f:
    f.write("New File Created")

# import os
# os.remove('Sex') # to remove a file which exist