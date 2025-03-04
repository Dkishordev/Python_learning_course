
#example 1
name=input("Enter your name: ")

while name=="":
    print("You didn't enter your name.")
    name=input("Enter your name: ")
print(f"Your name is {name}.")

food=input("Enter your favourite food (press q to quit): ")

while not food.lower()=="q":
    print(f"Your favourite food is {food}.")
    food=input("Enter your another favourite food (press q to quit): ")
print("Bye bye")

#example 2
num = 1
while num < 6:
  print(num)
  num += 1 

#simple program to calculate compound interest using while loop
principal =0
time=0
rate=0

while principal<=0:
    principal = float(input("Enter the principal amount: "))
    if principal<=0:
        print("Principal amount cannot be less than or equal to zero.")

while rate<=0:
    rate = float(input("Enter the interest rate: "))
    if rate<=0:
        print("Interest rate cannot be less than or equal to zero.")

while True:
    time = int(input("Enter the time in yeras: "))
    if time<=0:
        print("Time cannot be less than or equal to zero.")
    else:
       break

total = principal * pow((1 + rate/100),time)
print(f"Balance after {time} years is ${total:.2f}")