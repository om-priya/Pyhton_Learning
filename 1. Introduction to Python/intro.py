# PYTHON IS AWESOME

# How to declare a variable and print it
my_name = "Om Priya"
age = 21
print(my_name, age)

# Note: Don't declare variable names with numbers(start Mei)
# and don't use any special character

# In Maths --> BODMAS, In Python --> PEMDAS
# Division always result in Floating Point Number
print(12 / 3)
print(12 // 3)  # Removes everything after division

# % --> is used to calculate remainder
print(23 % 3)

# *********** STRINGS IN PYTHON ****************
my_string = "Om Priya"
my_string2 = 'Hey, How are "you? '
print(my_string2 + my_string)
# MultiLine Comment and MultiLine Strings
"""
Concatenation between string and number will throw type error not as js
"""
age = 21
age_in_str = str(age)
print(my_string + age_in_str)

# ********** STRING FORMATING ***********
# f string in python (kind of similar to template literals in js) above pyhton 3.6
random_name = "Shivam"
template = f"How are you {random_name}"
print(template)
random_name = "Om Priya"
# same as last one because python already processed the result and store it in template
print(template)
# How to resolve this issue --? We can use .format
# Also we can pass some name in {name} then .format(name) or .format(name = "Om Priya")
template2 = "How are you {}"
print(template2.format("Abhay"))

# ********** GETTING USER INPUT ***********
# By default input(something) will always be string so take care of that
# Also whenever you multiply a string with some num it will gice stringstring.....num times
age = int(input("Enter Your Age: "))
message = f"You are {age} years old"
print(message)

# *********** BOOLEANS AND COMPARISONS **********
# True False
user_age = 20
is_under_age = user_age < 18
is_over_age = user_age >= 18
is_20_age = user_age == 20
print(is_under_age, is_over_age, is_20_age)
# Note: 0 or any empty value such as empty string,list will always be false

# ************* AND OR IN PYTHON *****************
#                 SAME AS C++(which value it will return)
# Priority of and is > priority of or (left to right)
"""
            1   2   Which Value
FOR AND:    T   T       2
            T   F       2
            F   T       1
            F   F       1
FOR OR:     T   T       1
            T   F       1
            F   T       2
            F   F       2
"""
