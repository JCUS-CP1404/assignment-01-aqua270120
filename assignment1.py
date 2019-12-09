import csv
"""
Replace the contents of this module docstring with your own details
Name:Nguyen le huy bao
Date started:29/11/2019
GitHub URL:https://github.com/JCUS-CP1404/assignment-01-aqua270120
"""
# create a new list
movie_list = []
with open("movies_backup.csv", "r") as rf:
    reader = csv.reader(rf)
    movie_list = list(reader)
    # sort by year and add to the new list
    movie_list.sort(key=lambda movie_list: int(movie_list[1]))
print()


# print and count movies based on the third character
def print_list():
    movie_watch = 0
    movie_unwatch = 0

    for i, movie_data in enumerate(movie_list):
        if movie_data[3] == "u":
            print("{}. * {:<50s}     -{:5s}  ({})".format(i, movie_data[0], movie_data[1], movie_data[2]))
            movie_unwatch += 1
        if movie_data[3] == "w":
            print("{}.   {:<50s}     -{:5s}  ({})".format(i, movie_data[0], movie_data[1], movie_data[2]))
            movie_watch += 1
    print("\t" + "{} movies watched, {} movies still to watch".format(movie_watch, movie_unwatch))


# year validation
def year_validation():
    while True:
        try:
            year = int(input("Year:"))
        except ValueError:
            print("Invalid input. Enter a valid number")
            continue
        if year < 0:
            print("Number must be >= 0")
            continue
        else:
            print(year)
            break
    return int(year)


# genre validation
def genre_validation():
    while True:
        genre = input("Category: ").capitalize()
        if genre not in ("Action", "Adventure", "Comedy", "Drama", "Fantasy", "Historical", "Horror", "Mystery"
            , "Romance", "Political", "Thriller", "Urban", "Western", "Sci-Fi", "Saga", "Porn"):
            print("Not a valid genre.Please try again! ")
        else:
            print(genre)
            break
    return genre


# title validation
def title_validation():
    title = input("Title: ")
    if title.isdigit() is True:
        print("Title can not be a number")
        return title_validation()
    elif len(title) == 0:
        print("Title can not be blanked")
        return title_validation()
    else:
        print(title.strip())
    return title.strip()


# movies number validation
def movies_number(movie_list):
    while True:
        try:
            watch = int(input(">>>"))
        except ValueError:
            print("Invalid input. Enter a valid number")
            continue
        if watch < 0:
            print("Number must be >= 0")
            continue
        elif watch > len(movie_list):
            print("Invalid movie number")
        else:
            break
    return watch


# append new movie to the movie_list and sort by year
def add_movie():
    title = title_validation()
    year = year_validation()
    genre = genre_validation()
    print("{} ({} from {}) added to movie list ".format(title, genre, year))
    new_movie = [title, str(year), genre, "u"]
    movie_list.append(new_movie)
    movie_list.sort(key=lambda movie_list: int(movie_list[1]))


# check if there are movies to watch or not
def check_movie():
    for movie_data in movie_list:
        if movie_data[3] != "w":
            return False
    return True


# check if movie is watched or not
def watch_movie():
    if check_movie():
        print("No movies to watch")
    else:
        print("Enter the number of movie to mark as watched")
        watch = movies_number(movie_list)

        first_position = int(watch)
        if movie_list[first_position][3] == "w":
            print("You have already watch", movie_list[first_position][0])
        else:
            movie_list[first_position][3] = "w"
            print("{} from {} watched".format(movie_list[first_position][0], movie_list[first_position][1]))


def main():
    """..."""
    print("Movies To Watch 1.0 - by Nguyen Le Huy Bao")
    print("{} movies loaded".format(len(movie_list)))
    while True:
        print("\t-----Menu-----")
        print("(L)- List movies ")
        print("(A)- Add new movies ")
        print("(W)- Watch a movie ")
        print("(Q)- Quit ")
        # ask user to choose to play or instructions or quit
        choice = input(">>> ").upper()
        if choice == "L":
            print_list()
        elif choice == "A":
            add_movie()
        elif choice == "W":
            check_movie()
            watch_movie()
        elif choice == "Q":
            print("Thank you")
            print("{} movies saved to movies.csv".format(len(movie_list)))
            break
        else:
            print("Invalid menu choice. Please try a again ")

    # write movies_list to the movies and also to reset movies file
    with open("movies.csv", "w") as movie_backup:
        movies_writer = csv.writer(movie_backup)
        for movies_data in movie_list:
            movies_writer.writerow(movies_data)


main()
