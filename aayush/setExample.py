# set is collection enclosed in curly bracket.
# set is a unique collection and unordered 
# set is generally use for intersection , difference , union


set1={23,45,56,23}
set2={45,90,23}

print(set1)

#type
print(type(set1))

#intersect(same)
x=set1.intersection(set2)
print(x)

#difference
y=set2.difference(set1)
print(y)


#union(all sets combine)
z=set1.union(set2)
print(z)