#Arithmetic Operator(Calculations):
a,b=6,2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#remainder
print(a//b)#floor division
print(a**b)#exponential

print("------------------------------------")
#Relational Operator(Comparision)->if condition true ->true , false->false

c1=45
c2=89
print(c1==c2)#equal to (compare value equal )
print(c1<=c2)#less than equal to (compare value equal )
print(c1>=c2)# greater than equal to (compare value equal )
print(c1<c2)#less than (compare value equal )
print(c1>c2)#greater 
print(c1!=c2)#not equal

print("------------------------------------")


#Logical Operator->
# logical operator is used to check two conditions
# and (when both condition is true it give true otherwise false)
# or  (If anyone condition is true it give true otherwise it give false).
# not ( It reverse the given condition)

l1,l2,l3,l4=23,45,67,78

print(l1>l2 and l3<l4)#false
print(l1>l2 or l3<l4)#true
print(not(l1>l2 or l3<l4))#true

print("------------------------------------")

#membership operator->It check that given element is a part of 
# collection or data or not by giving true or false

names=["Ayush","Deepika","Vishal","Varun"]
print("ayush" not in names)