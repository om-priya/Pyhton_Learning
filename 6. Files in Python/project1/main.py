"""
Ask User for 3 friends
For each friend we will tell whether they are nearby
for each friend we will save their name to nearby_friends.txt
"""

# Taking user input for the friends
user_input = []
for num in range(3):
    name = input("Enter Your Friend Name: ")
    user_input.append(name)

# Read the content of files as list
try:
    friends_file = open("./friends.txt", "rt")
    friends_list = friends_file.readlines()
    friends_file.close()
except FileNotFoundError:
    print("File is not Available")
else:
    print(friends_list)

# Compare using two loops
nearby_friends = []
for friend in friends_list:
    last_index = len(friend) - 1
    friend = friend[0:last_index]
    for user_friend in user_input:
        if user_friend.lower() == friend.lower():
            nearby_friends.append(user_friend.title())

# Write Content in nearby_friends
write_file = open("./nearby_friends.txt", "wt")
write_file.writelines(nearby_friends)
write_file.close()
