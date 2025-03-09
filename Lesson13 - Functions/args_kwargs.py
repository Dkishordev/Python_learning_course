#  *args: allows to pass multiple non key arguments (tuple)
#  **kwargs: allows to pass multiple key arguments (dict)
# * unpacking operator
# 1) positional, 2) default, 3) keyword, 4) arbitary

# *args
def addnumbers(*args):
    total=0
    for arg in args:
        total += arg
    return total

sum = addnumbers(1,3,5)
print(sum)
print(addnumbers(1))
print(addnumbers(1,2,3,4,5))

def display_name(*names):
    for name in names:
        print(name, end=" ")
    print()

display_name("Mr","John","Doe")
display_name("John")
display_name("John","Doe")

# **kwargs

def emp_information(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

emp_information(name="John Doe",
                address ="123, street",
                phone ="23456279",
                salary="$2345",
                age="30")

emp_information(name="John Doe",
                address ="123, street",
                phone ="23456279",
                salary="$2345",
                status ="married",
                age="30")

# *args and **kwargs together
def empinformation(*args,**kwargs):
    print("============ Emp Info ================")
    for arg in args:
        print(arg, end=" ")
    print()
    print(f"{kwargs.get('apt')} {kwargs.get('address')}")
    print(f"{kwargs.get('city')} {kwargs.get('st')} {kwargs.get('zip')}")
""" 
    for key,value in kwargs.items():
        print(f"{key} : {value}") """

empinformation("Mr.","John","Doe",
                address ="Main Street",
                apt ="25A",
                city ="Fakecity",
                st="London",
                zip ="BM2 3ZG")
