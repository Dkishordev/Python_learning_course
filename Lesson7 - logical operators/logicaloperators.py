# Logical Operators in Python

var_a = True
var_b = False

# AND Operator: Returns True if both statements are true
and_result = var_a and var_b  # False
print("AND Operator:", and_result)

# OR Operator: Returns True if at least one statement is true
or_result = var_a or var_b  # True
print("OR Operator:", or_result)

# NOT Operator: Reverses the boolean value
not_result = not var_a  # False
print("NOT Operator:", not_result)

# Using logical operators with comparisons
num1 = 10
num2 = 5

# AND example
if num1 > 5 and num2 < 10:
    print("Both conditions are True")

# OR example
if num1 > 10 or num2 < 10:
    print("At least one condition is True")

# NOT example
if not (num1 < num2):
    print("num1 is not less than num2")


#conditional expressions
# aconcise way to write an if-else statement in a single line. also known as the ternary operator.
#syntax: value_if_true if condition else value_if_false

x = 10
y = 20

min_value = x if x < y else y
print(min_value)  # Output: 10

age= 16
agegroup ="Adult" if age >= 18 else "Child"
print(agegroup) #output Child

#nested example
a, b, c = 5, 10, 15

min_value = a if a < b and a < c else (b if b < c else c)
print(min_value)  # Output: 5