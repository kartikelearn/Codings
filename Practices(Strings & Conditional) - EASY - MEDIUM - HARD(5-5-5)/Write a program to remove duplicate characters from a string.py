#Write a program to remove duplicate characters from a string.
string=['mango',"apple",'mango','apple']
sen=string
string=list(set(string))
print(string)
# Method 2
unique_sen=list(dict.fromkeys(sen,0))  # When we convert a list into dictionary it only takes the keys of it
print(unique_sen)   