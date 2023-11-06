# ******* LIST, TUPLE, SET, DICTIONARY **********

# 1> Lists []
heroes = ["IronMan", "Captain", "Hulk", "Thor"]
print(heroes)
print(heroes[0])
heroes[1] = "Captain America"
print(heroes)
print(len(heroes))
heroes.append("Loki")
heroes.remove("Captain America")
print(heroes)

# List of Lists 2D Array
binary_matrix = [[0, 1, 0], [1, 1, 1], [1, 0]]
print(binary_matrix)

# 2> Tules () --> brackets are optional but in someplace it's mandatory.
my_tuple = "rob", "sky", "fly"  # ye tuple hai
my_tuple2 = ("rob", "sky", "fly")  # ye bhi tuple hai
my_tuple3 = ("rob",)  # bina comma ke string comma toh tuple
# can't append or remove any item from a tuple but look below example
my_tuple = my_tuple + my_tuple2
print(my_tuple)
# what happend here --> we didn't change my_tuple by concatinating we just created another tuple and assign those to my_tuple


# 3> SETS IN python --> {}
# sets don't hold order it means when you add the element it doesn't maintain order how to print it  and if you add duplicate element element in the set it won't give error it's just don't do anything
art_student = {"prem", "rahul", "modi"}
science_student = {"modi", "rahul", "arvind", "mamta"}
art_student.add("yogi")
science_student.remove("mamta")

# some advance opearation on sets (mathematics operation)
print(art_student.difference(science_student))  # A - B
print(art_student.union(science_student))  # A U B
print(art_student.intersection(science_student))  # A N B
print(art_student.symmetric_difference(science_student))  # not in both A U B - A N B

# *********** Dictionaries in Python ***************
# Dictionaries are ordered(after 3.7), changeable, don't allow duplicate elements
# if you know key you know the value (ex: let's make a tuple of dictionary)
# Unique Keys in a dict (mtlb ek curly braces ke andar)
my_dict = (
    {"name": "Om Priya", "age": 21},
    {"name": "Om Priya", "age": 21},
    {"name": "Shivam", "age": 15},
    {"name": "Kirmada", "age": 35},
)
print(my_dict)
print(my_dict[0])
print(my_dict[1]["name"])
my_dict[2]["name"] = "system"
print(my_dict[2]["name"])
print(my_dict)

# Quick Question --> Calculate the avd grades
grades = [80, 90, 78, 100, 96]
total = sum(grades)
length = len(grades)
avg = total / length
print(avg)

# ********** Join a list **************
friends = ["I", "Me", "Myself"]
and_separated = " & ".join(friends)
my_string = f"I only care about {and_separated}"
print(my_string)
