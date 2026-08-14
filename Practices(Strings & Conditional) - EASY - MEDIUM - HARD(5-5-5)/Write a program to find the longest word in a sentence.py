#Write a program to find the longest word in a sentence.
str=str(input("Enter the string here: "))
words=str.split()
longest_word=max(words, key=len)
print(longest_word)