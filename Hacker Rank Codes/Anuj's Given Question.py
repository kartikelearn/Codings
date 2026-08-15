#Check if occurence of two or more elements is same then Return True
l = [1,2,1,3,2,2]
# ul=set(l)
# ule=list(ul)
# null = []

# for el in ule:
#     null.append(l.count(el))
# print(null)
# print(len(set(null))<len(null))


#we can also use this module
from collections import Counter
freq = Counter(l)
print(len(freq.values()) != len(set(freq.values())))