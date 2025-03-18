
class Student:
    college_name="Paramount College"
    def __init__(self, name,marks):  #constructor
        self.name=name
        self.marks =marks

    @staticmethod
    def welcome():
        print("Welcome students")

    def function(self):
        print("This is a message inside the class.")
    
    def get_average_marks(self):
        sum=0
        sub_len=len(self.marks)
        for sub in self.marks:
            sum+=sub
        average=sum/sub_len
        print(f"The student {self.name} studying in {self.college_name} has {average} average marks.")

student1 = Student("John",[96,97,98])
student1.welcome()
student1.get_average_marks()
student2 = Student("Bob",[96,97,98,99,94])
student2.get_average_marks()
student2.function()