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
    required_fields = ["Title", "Year", "Ratings", "Poster"]

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Raise HTTPError for bad responses
        data = response.json()

        if data.get("Response") != "True":
            print(f"Movie not found: {title}")
            return {}
        # check for missing fields
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            print(f"Missing fields: {', '.join(missing_fields)}")
            return {}

        # Additional check for Rating being a list with at least one rating
        if not isinstance(data.get("Ratings"), list) or len(data.get("Ratings")) == 0:
            print(f"No ratings found for {title}")
            return {}

        return data

    except ConnectionError:
        print("Error: Unable to connect to the API. Please check your internet connection.")
        return {}
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to reach the API: {e}")
        return {}
