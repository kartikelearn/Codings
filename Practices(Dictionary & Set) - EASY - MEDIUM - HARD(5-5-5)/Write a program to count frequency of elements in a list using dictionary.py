#Write a program to count frequency of elements in a list using dictionary.
list=[1,2,3,2,2,3,4]
lst = [1, 2, 3, 2, 2, 3, 4]

freq = {}
# for i in range(len(list)):
#     el = list[i]
#     if el in freq:
#         freq[el] += 1  # if value exist then it add + 1 next turn
#     else:
#         freq[el] = 1   # if element come first time it store the value 1
# print(freq)

#or

for el in lst:
    freq[el] = freq.get(el, 0) + 1

print(freq)

#or

freq1={}
for el in lst:
    freq1[el]=lst.count(el)
    freq1.update({el:lst.count(el)})
print(freq1)

#### Wrong Approach

# x=1
# count=0
# dict={
#     "Sex":"Male",
#     "Orgasum":"G-Spot",
#     "Body-Count":29,
#     "list":list
# }
# print(dict)
# for el in dict["list"]:
#     if(el==x):
#         count+=1
# print(count)

# c=0
# #or
# value=dict.get("list")
# for el in value:
#     if(el==x):
#         c+=1
# print(c)
