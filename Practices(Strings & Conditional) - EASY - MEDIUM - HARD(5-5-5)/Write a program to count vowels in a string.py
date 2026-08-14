#Write a program to count vowels in a string.
str=str(input("Enter your string here: "))
print(str.count("a")+str.count("e")+str.count("i")+str.count("o")+str.count("u"))

text = input("Enter your string here: ")
print(sum(1 for ch in text.lower() if ch in "aeiou"))

count=0
for ch in text:
    if ch.lower() in "aeiou":  #Membership operator (checks presence)
        count+=1
print(count)