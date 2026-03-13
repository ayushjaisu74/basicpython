# dict : It is use to store data in key-value pair . curly bracket {key:value}
#we can access value using key , But cannot access key using value.


details={
   " name":"Ayush Jaiswal",
   "age":21,
   "course":"Python",
   "fees":12000,
}

print(details)

#type
print(type(details))


#key
print(details[" name"])


#get
print(details.get("fees"))


#keys
print(details.keys())

#values
print(details.values())