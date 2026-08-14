me={
    "Name":"Kartike",
    "Age":18,
    "Subject":["Maths","Science","SST","Hindi"]
}
print(type(me.keys()))
print(me.keys())    #1 return all keys
print(type(me.values())) 
print(me.values())  #2 return all values
print(type(me.items()))
print(me.items())  #3  return all pairs as tuples
pair=list(me.items())
print(pair[0])
print(me.get("Name")) # return the key according to value
print(me["Name"])
# # actually when we use get function it doesn't give any error if there is not any declared key -- None
# new_me={2:8}
# me.update(new_me)
# me.update({"K":"S"})  # Insert the specified items to the dictionary
# print(me)
# print(list(me.keys())) # typecasting
# print(tuple(me.keys())) # typecasting
# print(str(me.keys()))  # typecasting
# print(len(me))
# print(len(tuple(me.keys())))