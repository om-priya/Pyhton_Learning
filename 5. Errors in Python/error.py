# How does python show the error and how a developer should read it
"""
1> At the very bottom there is the type of error
2> Above that line that give that error
3> Which function give that error
4> who call that function
5> So on.............
"""
# ******** Built - In Errors **************
"""
1> IndexError (Acces index that didn't exists)
2> KeyError (Wrong Key to access value)
3> NameError (When var is not defined)
4> AttributeError (Performing some operation on something that doesn't support it (ex: intersection on lists))
5> NotImplementedError (Raise error when some feature is not implemented ex: raise NotImple...("SOme Message))
6> RuntimeError (Not clear when it happens basically a base class and other error classes inherit it)
7> SyntaxError (illegal syntax)
8> IndentationError (simple already know when indention is wrong)
9> TabError (decide whether to use space or tab for indentation)
10> TypeError (adding of int and string [+ is an function which is already defined that's why this error comes])
11> ValueError (conerting 20.5 of type string to int only built in errors throw value error)
12> ImportError ( basically A is importing b and b is importing c and c is importing a it will be in loop)
13> DeprecationWarning (something that is not supported in this version of python you are using)
Generally you won't raise these errors you will raise your own error with better name
"""

# ******** Raising a Error in Python **********
# syntac ----->
# raise TypeError("Some message")


# ****** Creating Custom Errors in Python *********
class CustomError(ValueError):
    def __init__(self, code):
        super().__init__(f"Error With Code {code}")
        self.code = code


# Error Handling using try and except with isinstance(object,Class) function
# Finally will always execute irrespective of try or catch also error stack will not shown in this case as we are catching it
# Note finally will always execute even if you return keyword in try or except but else will only execute if no return in try
class Students:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name(student):
        if not isinstance(student, Students):
            raise TypeError("The Object is Not of Students Class")
        else:
            print(student.name)


om_priya = Students("Om Priya")
try:
    om_priya.get_name("Hello")
except TypeError:
    print("Something went Wrong")
    # raise # (check comment at 62 line)
finally:
    print("Both Got Executed")

# But how do we see trace stack as it helps in finding the error in python
# Solution is we just type raise in except

# Suppose we want to run something onsuccess execution of the try block but we can't run finally because it will always run so for that you can use else block(onsuccess) but make sure you are not returning anything in try block

try:
    print("Hello")
except SyntaxError:
    print("Syntax is wrong")
else:
    print("Succesfull Execution")
