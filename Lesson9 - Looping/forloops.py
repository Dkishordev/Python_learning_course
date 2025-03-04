
for count in range(1,6):
    print(count)

for count in range(0,10,2):
    print(count )

for i in "Hello":
    print(i)

#escape 4 while printing
for count in range(1,6):
    if count ==4:
        continue
    else:
        print(count)

#prints upto 3
for count in range(1,6):
    if count ==4:
        break
    else:
        print(count)

import time

sec= int(input("Please input time in seconds: "))

for x in range(sec, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours =int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times Up!")