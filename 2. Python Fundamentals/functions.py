# Syntax of Function
# No Concept of Hoisting so order of function defining really matters here
# Note: If you try to store the value of function which is not returning anything it will store none
def greet():
    print("Hello There")


greet()

# Arguments and Parameters
# Global and Local Scope ---> Same as C++


# No return type
def proper_greet(name, message):
    template = f"Hey {name}, I've a small message for you: {message}"
    print(template)


proper_greet("Om Priya", "You are doing Great")
# Above Function have no return value


# ************ RETURN TYPE FUNCTIONS *****************
def divide(x, y):
    if y == 0:
        return "Can't divide by Zero"
    else:
        return x / y


print(divide(10, 5))
print(divide(10, 0))


# ************** Default and Named Parameter *****************
def add(x, y=3):
    total = x + y
    return total


print(add(2, 4))
print(add(2))
print(add(x=2, y=5))
# Note: all the default parameter and named arguments should be declare at last
# it means that all the subsequent parameter or arguments should be default or named

# ************ Lambda Functions *****************
# When you doing one thing

response = lambda req_data: f"Data Recieved: {req_data}"
print(response("Hello"))
# Very wierd syntax try to avoid it
print((lambda x, y: x + y)(10, 3))

"""
First Class Functions
First class objects in a language are handled uniformly throughout. They may be stored in data structures, passed as arguments, or used in control structures. A programming language is said to support first-class functions if it treats functions as first-class objects. Python supports the concept of First Class functions.

Properties of first class functions:

A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, 
"""


def say_hello():
    print("hello")


def say_namaste():
    print("Namaste")


def say_hi():
    print("Hi")


greetings = {
    "hello": say_hello,
    "namaste": say_namaste,
    "hi": say_hi,
}

say_something = input("What do you want me to say? ")
say_something = say_something.lower()
greetings[say_something]()
