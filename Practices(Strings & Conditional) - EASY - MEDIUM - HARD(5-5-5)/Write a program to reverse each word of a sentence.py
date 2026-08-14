#Write a program to reverse each word of a sentence.
sentence = "My name is kartike"

words = sentence.split()

reversed_words = []
print(type(reversed_words))

for word in words:
    reversed_words.append(word[::-1])
print(type(reversed_words))
result = " ".join(reversed_words)
print(type(result))
print(result)




