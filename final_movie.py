import statistics
import random
import difflib

import matplotlib.pyplot as plt

from colorama import Fore
import persistant_movie_storage

colors = {
    'error': Fore.RED,
    'info': Fore.MAGENTA,
    'menu': Fore.GREEN,
    'title': Fore.LIGHTBLUE_EX,
    'input': Fore.LIGHTWHITE_EX,
}


def main():
    """Entry point of the program. Initializes the movie database and starts the menu loop."""
    print(colors['title'] + "********** My Movies Database **********" + "\n")
    movies = persistant_movie_storage.get_movies()
    choose_menu(movies)



def choose_menu(movies):
    """
    Displays the main menu and handles user input
    to perform various operations on the movie database.

    Args:
        movies (dict): The movie database.
    """
    menu = ["0. Exit",
            "1. List movies",
            "2. Add movie",
            "3. Delete movie",
            "4. Update movie",
            "5. Stats",
            "6. Random movie",
            "7. Search movie",
            "8. Movies sorted by rating",
            "9. Movies sorted by year",
            "10. Filter movies",
            "11. Create histogram"]
    while True:
        print(colors['menu'] + "Menu:\n" + "\n".join(menu) + "\n")
        try:
            user_choice = input(Fore.LIGHTWHITE_EX + "Enter choice (0-11): ")
            if user_choice == "0":
                print("Good Bye!")
                break
            elif user_choice == "1":
                print(list_movies(movies))
            elif user_choice == "2":
                print(add_movie(movies))
            elif user_choice == "3":
                print(delete_movie(movies))
            elif user_choice == "4":
                print(update_movie(movies))
            elif user_choice == "5":
                print(stats(movies))
            elif user_choice == "6":
                print(random_movie(movies))
            elif user_choice == "7":
                print(search_movie(movies))
            elif user_choice == "8":
                print(sorted_movies_by_rate(movies))
            elif user_choice == "9":
                print(sorted_movies_by_year(movies))
            elif user_choice == "10":
                print(filter_movies(movies))
            elif user_choice == "11":
                print(create_histogram(movies))

            input(colors['input'] + "Press enter to proceed" + "\n")
        except ValueError:
            print("Please enter a number (0-11)!")
            continue


def list_movies(movies):
    """
    Lists all movies in the database along with their ratings and release years.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A formatted string listing all movies with their details.
    """
    movie_list = []

    for title, details in movies.items():
        movie_list.append(f"{title}: {details['Rating']} -- (Year:{details['Year']})")
    movie_output = '\n'.join(movie_list)

    return f"{colors['info']}Total count of Movies:{len(movie_list)}\n{movie_output}"


def add_movie(movies):
    """
    Adds a new movie to the database after prompting the user for details.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A message indicating the result of the operation.
    """
    movie_to_add = input("Enter Movie name you want to add: ")

    if movie_to_add in movies:
        return f"{colors['error']}Movie already exists, going back to menu..."
    elif movie_to_add == "":
        return (f"{colors['error']}No empty Input allowed."
                f" Your Movie needs to be at least one char."
                f" long! Going back to menu...")

    try:
        rate_to_add = float(input("Enter a rate to the chosen Movie (0-10): "))
        year_to_add = int(input("Enter the Year of the Movie: "))
        movies[movie_to_add] = {"Rating": rate_to_add, "Year": year_to_add}



    except ValueError:
        return f"{colors['error']}Invalid input. Rating must be a number (e.g. 8.5), year must be a number(e.g. 7)."

    try:
        persistant_movie_storage.add_movie(movie_to_add, rate_to_add, year_to_add)
    except Exception as e:
        return f"{colors['error']}Something went wrong while saving: {str(e)}"

    return f"{colors['info']}Movie menu successfully add {movie_to_add}"


def delete_movie(movies):
    """
      Deletes a movie from the database based on user input.

      Args:
          movies (dict): The movie database.

      Returns:
          str: A message indicating the result of the operation.
      """
    movie_to_del = input("Enter a Movie you want to delete from the Movie menu: ")

    if movie_to_del in movies:
        del movies[movie_to_del]
        persistant_movie_storage.delete_movie(movie_to_del)
        return f"{colors['info']}The movie {movie_to_del} was deleted successfully"
    else:
        return f"{colors['error']} The Movie doesnt exist."


def update_movie(movies):
    """
    Updates the rating of an existing movie in the database.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A message indicating the result of the operation.
    """
    movie_to_update = input("Enter a Movie to update its rate: ")

    if movie_to_update in movies:
        try:
            enter_new_rate = float(input('Enter a new rate: '))
            movies[movie_to_update]['Rating'] = enter_new_rate
            persistant_movie_storage.update_movie(movie_to_update, enter_new_rate)
            return (f"{colors['info']}The rating of the movie '{movie_to_update}' "
                    f"was successfully updated.")
        except ValueError:
            return f"{colors['error']}Invalid input. Please enter a numeric value for the rating."
    else:
        return f"{colors['error']}The chosen movie does not exist."


def stats(movies):
    """
    Calculates and displays statistical information about the movie ratings.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A formatted string containing average, median, best, and worst movie ratings.
    """
    rate_list = [details['Rating'] for details in movies.values()]

    average_rate = statistics.mean(rate_list)
    median_rate = statistics.median(rate_list)

    max_rating = max(rate_list)
    min_rating = min(rate_list)

    best_movies = [f"{title}, {details['Rating']}"
                   for title, details in movies.items() if details['Rating'] == max_rating]
    worst_movies = [f"{title}, {details['Rating']}"
                    for title, details in movies.items() if details['Rating'] == min_rating]

    return (f"{colors['info']}The average rating is: {average_rate:.2f}\n"
            f"The median rating is: {median_rate:.2f}\n"
            f"The best movie(s):\n" + '\n'.join(best_movies) + "\n"
                                                               f"The worst movie(s):\n" + '\n'.join(worst_movies))


def random_movie(movies):
    """
    Selects and displays a random movie from the database.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A formatted string with the selected movie's title and rating.
    """
    title, details = random.choice(list(movies.items()))
    return f"{colors['info']}The movie of the night: {title}, Rating: {details['Rating']}"


def search_movie(movies):
    """
    Searches for movies containing a user-provided substring in their titles.
    Suggests similar titles if no exact matches are found.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A formatted string with search results or suggestions.
    """
    user_search = input("Enter a part of the movie title: ")
    potential_matches = [(title, details) for title, details in movies.items()
                         if user_search.lower() in title.lower()]

    if potential_matches:
        return "\n".join([f"{colors['info']}{title}, Rating: {details['Rating']}, Year: {details['Year']}"
                          for title, details in potential_matches])

    titles_list = list(movies.keys())
    suggestions = difflib.get_close_matches(user_search, titles_list, n=3, cutoff=0.6)

    if suggestions:
        suggestion_output = [f"{colors['info']}- {title}" for title in suggestions]
        return (f"{colors['error']}The movie '{user_search}' does not exist.\n"
                f"{colors['info']}Did you mean:\n" + "\n".join(suggestion_output))
    else:
        return f"{colors['error']}No similar movies found."


def sorted_movies_by_rate(movies):
    """
    Sorts and displays movies by their ratings in descending order.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A formatted string listing movies sorted by rating.
    """
    sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]['Rating'], reverse=True))
    output_descending_order = "\n".join([f"{title}, Rating: {details['Rating']}, Year: {details['Year']}"
                                         for title, details in sorted_movies.items()])
    return f"{colors['info']}Movies sorted by descending rating:\n{output_descending_order}"


def sorted_movies_by_year(movies):
    """
    Asks the user for descending or ascending order and Sorts the movies by year in the order chosen by the user.

    Args:
        movies (dict)
    Returns:
        str: A formatted string Listing movies sorted by year.
    """
    user_order = input("If you would like an descending order, enter 'd'.\n"
                       "If you would like an ascending order, enter 'a': ")
    if user_order.lower() == "d":
        sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]['Year'], reverse=True))
        output_descending_order = "\n".join([f"{title}, Rating: {details['Rating']}, Year: {details['Year']}"
                                             for title, details in sorted_movies.items()])
        return f"{colors['info']}Movies sorted by descending year:\n{output_descending_order}"

    elif user_order.lower() == "a":
        sorted_movies = dict(sorted(movies.items(), key=lambda item: item[1]['Year'], reverse=False))
        output_ascending_order = "\n".join([f"{title}, Rating: {details['Rating']}, Year: {details['Year']}"
                                             for title, details in sorted_movies.items()])
        return f"{colors['info']}Movies sorted by ascending year:\n{output_ascending_order}"
    else:
        return (f"{colors['error']}You need to enter 'a' for ascending order or 'd' for descending order!"
               f"No other input is valid. Going back to menu...")


def filter_movies(movies):
    """
    Asks the user for minimal rating, start and end year,
    for filtering the possible movies. If an input leaves empty,
    no limitation on that filter.

    Args:
         movies(dict)
    Returns:
         the filtered movies with rating and year
    """
    filtered_movies = []

    min_rating_input = input("Enter minimum rating (leave blank for no minimum rating): ")
    start_year_input = input("Enter start year (leave blank for no start year): ")
    end_year_input = input("Enter end year (leave blank for no end year): ")

    try:
        minimum_rating = float(min_rating_input) if min_rating_input else 0
    except ValueError:
        print(f"{colors['error']} Minimum rating must be a number. Using 0 as default.")
        minimum_rating = 0

    try:
        start_year = int(start_year_input) if start_year_input else float('-inf')
    except ValueError:
        print(f"{colors['error']} Start year must be an integer. Using no lower bound.")
        start_year = float('-inf')

    try:
        end_year = int(end_year_input) if end_year_input else float('inf')
    except ValueError:
        print(f"{colors['error']} End year must be an integer. Using no upper bound.")
        end_year = float('inf')

    for title, detail in movies.items():
        if start_year <= detail['Year'] <= end_year and detail['Rating'] >= minimum_rating:
            filtered_movies.append(f"{title} ({detail['Year']}): {detail['Rating']}")

    return f"{colors['info']}{'\n'.join(filtered_movies)}"


def create_histogram(movies):
    """
    Creates and saves a histogram of movie ratings.

    Args:
        movies (dict): The movie database.

    Returns:
        str: A message indicating the histogram has been saved.
    """
    try:
        output_file = input("Enter a filename to save the histogram (e.g., 'histogram.png'): ")
        ratings = [details['Rating'] for details in movies.values()]

        # Plot the histogram
        plt.hist(ratings, bins=5, color='lavender', edgecolor='black')
        plt.title("Movie Ratings Histogram")
        plt.xlabel("Rating")
        plt.ylabel("Number of Movies")

        # Save the histogram before showing it
        plt.savefig(output_file)
        plt.show()
        plt.close()
        plt.clf()

        return f"{colors['info']}Histogram saved as {output_file}"
    except Exception:
        print(f"{colors['error']} Something went wrong while saving the histogram.")

if __name__ == "__main__":
    main()
