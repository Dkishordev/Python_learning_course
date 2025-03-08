from prettytable import PrettyTable 
foods={"pizza": "10.0",
       "burger":"8.00",
       "chips":"7.65",
       "pasta":"6.0",
       "nachos":"3.5"
}
cart=[]
quantities =[]
total=0
print("============== Menu ==============")
for key,value in foods.items():
    print(f"{key:10}:  {value}")
print("==================================")


while True:
    food=input("Enter the food item you want to buy (q to quit): ")
    if food.lower()=="q":
        break
    elif foods.get(food) is not None:
        quantity =int(input(f"Enter the quantity of the {food}:"))
        cart.append(food)
        quantities.append(quantity)
print()

# specify the Column Names while initializing the Table 
if len(cart) !=0:
    table = PrettyTable(["Items",  "Quantity", "Price","Total"]) 
    for i in range(0, len(cart)):
        table.add_row([cart[i] , quantities[i],foods.get(cart[i]),float(foods.get(cart[i]))*quantities[i]])
        total+= float(foods.get(cart[i]))*quantities[i]
    print(table)
    print("============== Total  ==============")
    print(f"Your total is: ${total:.2f}")
else:
    print("You didn't order anything.")