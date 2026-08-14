my={
    "Name":"Kartike",
    "Age": 18,
    "Roll":"25BCON2280", # There is no indexing in Dictionary
    "Sec":"M",           # The elements can be changed like lists
}
print(type(set(my)))
print(my)                   # Duplicate keys are not allowed
print(my["Name"])           # To access a dictionary we use their key cause there is no indexing here   
my["Bodycount"]=0           # To Assign new key and value in a dictionary
print(my)
my["Name"]="Karan" # Overwrite // Update
print(my)
null_dict={}


