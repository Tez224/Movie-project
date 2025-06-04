import json

def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """
    try:
        with open("movie_file.json", "r") as file:
            movie_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        movie_data = {}

    return movie_data

def save_movies(movies: dict) -> None:
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("movie_file.json", "w") as file:
        json.dump(movies, file, indent=4)



def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    data = get_movies()

    data[title] = {"Year": year, "Rating": rating}

    save_movies(data)



def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    data = get_movies()

    if title in data:
        del data[title]
        save_movies(data)


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    data = get_movies()

    data[title] = {"Rating": rating}

    save_movies(data)