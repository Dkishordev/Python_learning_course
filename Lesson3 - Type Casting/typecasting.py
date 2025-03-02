#typecasting : the process of converting one data type to another
#string
first_name = "John"
last_name ="Doe"

#integer
age = 20

#float
salary = 3045.56

#bool
married = False

#finding type of variable
print(type(first_name))
print(type(age))
print(type(salary))
print(type(married))

#typecasting
age= float(age) # converts to float value
salary = int(salary) # converts to int value
print(age,salary)


#to string
age = 20
age= str(age)
print(age)
print(type(age))

#to bool
name="John"
name= bool(name)
print(name) # prints true

surname=""
surname= bool(surname)
print(surname)  # prints false

