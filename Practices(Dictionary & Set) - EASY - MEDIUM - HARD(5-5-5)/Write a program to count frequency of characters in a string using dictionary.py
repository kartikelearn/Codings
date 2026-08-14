#Write a program to count frequency of characters in a string using dictionary.
string = "Kartike"

freq = {}

for i in range(len(string)):
    ch = string[i]
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)