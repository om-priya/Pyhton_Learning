"""
This Program is used to store user's movies and the functionality are list,add, find

movies structure {
 "title"
 "director"
 "year"
}
"""
# List to store all the movies
movies = []


# Display Movies Name
def list_movies():
    for index in range(len(movies)):
        heading = movies[index]["title"]
        print(heading.title(), end=" ")
    print("")


# Add Movie to the List
def add_movie():
    title = input("Give title: ")
    director = input("Give director: ")
    year = input("Give year: ")

    movies.append(
        {
            "title": title.lower(),
            "director": director.lower(),
            "year": int(year),
        }
    )

    print("List Updated")
    print("")


# Find Movie By Title
def find_movie_by_title():
    title_to_find = input("Enter title to find? ").lower()
    for movie in movies:
        if movie["title"] == title_to_find:
            print(movie)
            break
    else:
        print("Movie Not Found")
    print("")


def main():
    print("****** Welcome Human ******")
    user_input = input("What do you want to do? (list,add,find,quit)")
    while user_input != "quit":
        if user_input == "list":
            list_movies()
        elif user_input == "add":
            add_movie()
        elif user_input == "find":
            find_movie_by_title()
        else:
            print("Wrong Input")
        print("")
        user_input = input("What do you want to do? (list,add,find,quit)")

    print("Thank You")


main()
