#"""list is collection of items enclosed in square bracket. list is  mutable data (update ,add ,delete ,sort)
# append()->Adding element in end.
# insert()->It is used to add in specific index.
# extend()->it extend  given list with another list 
# sort()->It is used to sort elements ascending order
# reverse()->It is used to reverse the order.
# pop()->It is used to remove element from last
# 
# 
# """


animal=["Tiger","Lion","Monkey","Elephant","Bear","Kangaroo"]
print(animal)

#type
print(type(animal))

#append
animal.append("Rino")
print(animal)


#insert
animal.insert(2,"Panda")
print(animal)

#
domestic_animal=["Cow","Buffalo","Cat","Dog"]
animal.extend(domestic_animal)
print(animal)


#sort (ascending order)
animal.sort()
print(animal)

#reverse(descending)
animal.reverse()
print(animal)


#pop:It remove element from last
animal.pop()
print(animal)

#remove
animal.remove("Cow")
print(animal)