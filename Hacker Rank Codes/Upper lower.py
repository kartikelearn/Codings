string = input()

isalnum = isalpha = isdigit = islower = isupper = False

for c in string:
    if c.isalnum():
        isalnum = True
    if c.isalpha():
        isalpha = True
    if c.isdigit():
        isdigit = True
    if c.islower():
        islower = True
    if c.isupper():
        isupper = True

print(isalnum)
print(isalpha)
print(isdigit)
print(islower)
print(isupper)