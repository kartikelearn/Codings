set={1,2,3,4,5}
set.add(6) # Add a number
print(set)
set.remove(1) # Remove a number
print(set)
set1=set.copy()
set1=list(set1)
set1.reverse()
print(set1)
print(list(set)==set1)
set.pop() # It deletes a random number// but i saw that it is deleting the 1st element
print(set)
print(set.pop())
print(set)
set.clear() # Clear a set
print(set)

seta={2,5,8,0}
setb={1,3,7,9}
print(seta.union(setb))
print(seta.intersection(setb))
