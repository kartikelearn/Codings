#Write a program to create a dictionary from two lists (keys list and values list).
key_list=["Kartike","Ayush","Nischal"]
value_list=[13,23,20]
dict={}
for i in range(len(key_list)):
    for j in range(i+1):  # range(start,stop-1,step)
       dict.update({key_list[i]:value_list[j]})
print(dict)