 
#Type 1: passing argument and returning value
def create_name(firstname, lastname):
    full_name=firstname.capitalize()+  " " + lastname.capitalize()
    return full_name

first_name="john"
second_name="doe"
fullname = create_name(first_name,second_name)
print(fullname)

#Type 2: passing argument and but no return type
def create_name(firstname, lastname):
    full_name=firstname.capitalize()+  " " + lastname.capitalize()
    print(full_name)

first_name="john"
second_name="doe"
create_name(first_name,second_name)


#Type 3: passing no argument and  but returning value
def create_name():
    firstname="john"
    lastname="doe"
    full_name=firstname.capitalize()+  " " + lastname.capitalize()
    return full_name

fullname = create_name()
print(fullname)


#Type 4: passing no argument and  but return type
def create_name():
    firstname="john"
    lastname="doe"
    full_name=firstname.capitalize()+  " " + lastname.capitalize()
    print(full_name)

create_name()