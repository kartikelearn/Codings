# Write a program to count how many times a word appears in a sentence.
sentence="My name is kartike kartike plays ff."
word = input("Enter word to count: ")
words=sentence.split()
count = words.count(word)
print(word, "appears", count, "times")


