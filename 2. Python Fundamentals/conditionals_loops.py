# ************* IF - ELSE *****************
# age = int(input("Enter Your Age: "))
age = 23
if age >= 18:
    print("You are Alive!")
elif age < 18 and age > 0:
    print("Still a kid")
else:
    print("You are not born yet!")

# *********** WHILE LOOP ***********
cnt = 0
while cnt < 5:
    inner_cnt = 0
    while inner_cnt < 5:
        print("*", end=" ")
        inner_cnt += 1
    cnt += 1
    print("")

print("Loop Ended")

# *********** FOR IN LOOP ***********
friends = ["Sharukh", "Salman", "Amir"]
for friend in friends:
    print(friend, end=" ")
print("")
for index in range(5):
    print(index, end=" ")
print("")

# Destructing in Python
friends = [
    ("ryan", 21),
    ("sky", 16),
    ("system", 25),
]
for name, age in friends:
    print(f"{name} is {age} years old")

# Iterating Over Dictionary
# By default we iterate over keys and to access values just put .values() and for both key and value put .items()
my_dict = {"ryan": 21, "sky": 19, "system": 27}
for key in my_dict:
    print(key, end=" ")
print("")
for value in my_dict.values():
    print(value, end=" ")
print("")
for key, value in my_dict.items():
    print(f"{key} is {value} years old")

# Break and Continue already know

# Note --> We can use else keyword with for loop else keyword will execute
# if the for loop will run completely without any error or break statements
