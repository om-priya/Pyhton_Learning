# How to read a file in python
# Try to reduce the time the file is open
# syntax for open(file_path, mode)
"""
Different Methods:
r -> read file (error if file is not there)
a -> open file for appending (create new file  if file not exists)
w -> open a file for writing (create the file if not exists)
x -> create the file and returns error if file exists

We can also specify as text or binary
t -> text
b -> binary

"rt" by default mode
"""
my_file = open("./demo.txt", "r")
file_content = my_file.read()
my_file.close()
print(file_content)

user_input = input("Enter your name: ")
# Note that w over writes your file
write_file = open("./demo.txt", "w")
write_file.write(user_input)
write_file.close()

# Now whenever we are opening the file we are also closing it which makes it irritating so what we can do is that we can something called with syntax what it do is that through that indented block your code will execute and then it will automatically close it (context managers)

with open("./project1/friends.txt", "r") as file:
    content = file.read()
print(content)
