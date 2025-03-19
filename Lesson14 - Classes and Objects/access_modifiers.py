class Person:
    def __init__(self,name,dob):
        self.name=name
        self.__dob=dob #private 

    def __find_dob(self): #private function can't be accessed from outside of class 
        return self.__dob
    
    def ispersonallowed(self):
        get_dob= self.__find_dob()  #private function can be accessed within the class
        if get_dob < 2007:
            print(f"{self.name} is allowed to enter the bar.")
        else:
            print(f"{self.name} is not allowed to enter the bar.")

p1= Person("Bob",2008)
p1.ispersonallowed() 
p2= Person("Joe",2006)
p2.ispersonallowed() 
