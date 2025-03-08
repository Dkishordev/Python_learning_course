
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))

mylist.remove("banana")
print(mylist)

mylist.append("orange") #add more list items
mylist.append("banana")
print(mylist)

mylist.insert(0,"grapes")


print(mylist[0])
print(mylist[2])

print(mylist[:-1])

mylist.sort()
print(mylist)

for fruit in mylist:
    print(fruit)

mylist.sort()

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)

#2D lists
fruits=  ["apple", "banana", "cherry"]
vegetables=["beans","potatoes","spanish"]
meats=["fish","chicken","buff"]
groceries=[fruits,vegetables,meats]

print(groceries)
print(groceries[1])
print(groceries[2][1])

for collection in groceries:
    for item in collection:
        print(item)