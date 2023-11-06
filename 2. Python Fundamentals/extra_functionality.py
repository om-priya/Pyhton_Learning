# ********** List Slicing ***************
# can be used with tuple,string as well
# Steps size (check further)
# To print in reverse [start:end:step_size] step_size = -1
friends = ["Sharukh", "Salman", "Amir", "Imran", "Manoj"]
print(friends[2:4])
print(friends[2:])
print(friends[:4])
print(friends[-3:])

# ************ List Comprehension ************
# Don't have to be list it can be any iterable object
friends = ["Sharukh", "Salman", "Amir", "Imran", "Manoj"]
friends_upper = [friend.upper() for friend in friends]
print(friends_upper)

# List Comprehension (I will use for in loop) with if statements
ages = [22, 81, 21, 17, 20]
odd_ages = [age for age in ages if age % 2 != 0]
print(odd_ages)

# *********** Set and Dictionary Comprehensions ******************
# Set Comprehension is almost similar to list comprehension the only diff is we are
# returning set

# Dictionary Comprehension
yaara = ["Susant", "Rounit", "Raja", "Mohan"]
time_since_seen = [1, 2, 0, 0]

long_timers = {
    yaara[i].lower(): time_since_seen[i]
    for i in range(len(yaara))
    if time_since_seen[i] > 0
}
print(long_timers)

# Zip Functions (combines the parameters of zip and made it in tuple)
# if you want to convert zip to dict make sure to pass only 2 parameters
long_timers = list(zip(yaara, time_since_seen, [1, 2, 3, 4]))
print(long_timers)

# enumerate function in python to provide with numbers/indexes print(enumerate(something)) will give the address of that object
yaara = ["Susant", "Rounit", "Raja", "Mohan"]

with_number = list(enumerate(yaara))
print(with_number)
with_number = dict(enumerate(yaara, start=1))
print(with_number)
