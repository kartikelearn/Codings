with open("practice.txt","r+") as f:
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)
with open("practice.txt","w+") as f:
    f.write(data.replace("Java","Python"))