
for x in range(1,6):
    for y in range(1,x+1):
        print("*", end=" ")
    print("")

for x in range(1,6):
    for y in range(1,x+1):
        print(y, end=" ")
    print("")

for x in range(1,6):
    for y in range(1,x+1):
        print(x, end=" ")
    print("")

for x in range(6,1,-1):
    for y in range(1,x):
        print(y, end=" ")
    print("")