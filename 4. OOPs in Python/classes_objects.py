class Student:
    # You can self whatever you want but it's still will be self
    def __init__(self, name, college, cgpa):
        self.name = name
        self.college = college
        self.cgpa = cgpa

    def show_info(self):
        print(self.name, self.college, self.cgpa, sep=" - ")

    def update_cgpa(self):
        new_cgpa = int(float(input("Enter Your New cgpa: ")))
        self.cgpa = new_cgpa


student_one = Student("Om Priya", "MUJ", 9.31)
student_two = Student("Piyush Kumar", "MUJ", 8.93)

print(student_one)
print(student_one.__class__)
print(student_one.show_info())  # Why none because not returning anything
student_one.show_info()

student_two.show_info()
# student_two.update_cgpa()
student_two.show_info()  # In background what does this look like Student.show_info(student_two)

# Note: so we can also create methods outside the class and instead of passing self we pass the object
# and then we can access it's variables


# ********* Magic Methods In Python *************(Good for understanding not for industry applications)
# Note: When you initiate some magic functions you can use for in loop
# repr is used for debugging and show object for developer and str is for user only
class Employee:
    def __init__(self, salaries):
        self.salaries = salaries

    def __str__(self):
        return f"Salarie are {self.salaries}"

    def __len__(self):
        return len(self.salaries)

    def __repr__(self):
        return "Calling through repr"


tech_employee = Employee([10, 20, 30, 40])
print(tech_employee)
print(len(tech_employee))


# *********** INHERITANCE IN PYTHON *******************
class Student:
    def __init__(self, name, college):
        self.name = name
        self.college = college

    def shout(self):
        print(f"{self.name} from {self.college} just shouted")


class WorkingStudent(Student):
    # def __inti__(self, name, college, company):
    #     self.name = name
    #     self.college = college
    #     self.company = company
    # But wouldn't it be better if we just have to do slef.company yes there is a way
    # super method to call functionality of parent class
    def __init__(self, name, college, company):
        super().__init__(name, college)
        self.company = company

    def got_placed(self):
        super().shout()
        print(f"{self.name} just got placed in {self.company} and stopped shouting")


student_one = WorkingStudent("Om Priya", "MUJ", "Watchguard")
student_one.shout()
student_one.got_placed()


# ****** Property decorator in python *************
class Student:
    def __init__(self, name):
        self.name = name

    @property
    def say_hello(self):
        print(f"Hello {self.name}")


# Now notice there is a function with only self as an argument so let's create an object
student_one = Student("Om Priya")
# student_one.say_hello()  # will print Hello Om Priya
# What happent if i do student_one.say_hello
student_one.say_hello  # will give bound method and show the address of the function
# After adding @property it will execute the method

# ***** Static Method and Class Method *******
"""
Whenever an a method is call there is 3 way to call it
1> Instance Method (obj will get passed as a parameter normal methods in class)
2> Class Method (class will get passed as parameter cls refer to class and you can call that function either through obj or class itself)
3> Static Method (Sometimes a method doesn't require class or obj to do it's work so declare those as static method)
Community Suggestion try to use classmethod and just don't use that variable (cls)
"""


class Company:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def greet_world():
        print("Hello World")

    @classmethod
    def class_name(cls):
        print(cls.__name__)


watchguard = Company("Watchguard")
Company.greet_world()
watchguard.greet_world()
Company.class_name()
watchguard.class_name()
