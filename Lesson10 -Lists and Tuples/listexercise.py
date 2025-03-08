from prettytable import PrettyTable 
foods=[]
prices=[]
quantities =[]
total=0

while True:
    food=input("Enter the food you want to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price =float(input(f"Enter the price of the {food}:"))
        quantity =int(input(f"Enter the quantity of the {food}:"))
        foods.append(food)
        prices.append(price)
        quantities.append(quantity)
print()
if len(foods)!=0:
    print("============== Items Details ==============")

    # specify the Column Names while initializing the Table 
    table = PrettyTable(["Items", "Price", "Quantity", "Total"]) 
    for i in range(0, len(foods)):
        table.add_row([foods[i],prices[i] , quantities[i],  prices[i]*quantities[i]]) 
        total += prices[i]*quantities[i]
    print(table)
    print("============== Total  ==============")
    print(f"Your total is: ${total:.2f}")
else:
    print("You didn't order anything.")