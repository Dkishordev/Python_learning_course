
collection ={
    "fruit":"apple",
    "meat":"chicken",
    "food":"pizza",
    "vegetables":"potato"
}

print(collection)
print(collection.get("fruit"))
print(collection.get("drinks"))
collection.update({"drinks":"soda"})
collection.update({"food":"burger"})
print(collection)

for key in collection.keys():
    print(key)

for value in collection.values():
    print(value)

for key,value in collection.items():
    print(f"{key}:{value}")