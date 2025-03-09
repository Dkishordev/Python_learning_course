import time
def count(end, start=0):
    for i in range(start,end):
        print(i+1)
        time.sleep(1)
    print("Done!")

count(5)
#count(5,2)

def create_name(firstname, lastname=""):
    full_name=firstname.capitalize()+  " " + lastname.capitalize()
    return full_name

first_name="john"
second_name="doe"
fullname = create_name(first_name,second_name)
print(fullname) # prints John Doe
print(create_name("boby")) # prints Boby


#keyword arguments

def createname(greeting,title,firstname, lastname):
    namestr=greeting+ " " + title+ " "+firstname+" "+lastname
    return namestr

print(createname("Hello","Mr.","John","Doe"))
print(createname("Hello", lastname="Jane",title="Ms",firstname="Susan"))
#print(createname( lastname="Jane",title="Ms",firstname="Susan","Hello")) -- error code