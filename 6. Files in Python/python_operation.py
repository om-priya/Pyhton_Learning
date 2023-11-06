# To write in file
def save_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


# To read from file
def read_file(filename):
    with open(filename, "r") as file:
        return file.read()
