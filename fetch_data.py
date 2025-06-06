import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_movie_by_title(title):
    """
    Fetch movie data by title from OMDB API.
    :param title: Movie title to search for.
    :return: The movie data as a dictionary or an empty dictionary if not found.
    """
    url = f"https://www.omdbapi.com/?apikey={API_KEY}"
    params = {"t": title}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("Response") == "True":
            return data  # Return the entire movie data if found
        else:
            print(f"Movie not found: {title}")
            return {}  #
    except ConnectionError:
        print("Error: Unable to connect to the API. Please check your internet connection.")
        return {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to reach the API: {e}")
        return {}