#Write a program to find symmetric difference between two sets.
set1={1,2,3,4}
set2={4,5,6,7}

# Symmetric difference mtlb jo common part ho i mean jo intersect ho woh element final set me n ho
intersect=set1.intersection(set2)
union=set1.union(set2)
sd=union-intersect
print(sd)

# We have also a shortcut for doing that
fset=set1.symmetric_difference(set2)
print(fset)