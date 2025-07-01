# Movie Mountain - A Movie Collection App

## Overview

Welcome to **Movie Mountain**, a simple movie collection app that allows you to browse, add, and display movies stored in a SQLite database. The application fetches movie details from an external API, stores them in a local database, and displays them in a web interface.

## Features

- **Add Movies**: Add new movies by providing a title. The movie details (including rating and poster) are fetched automatically using an API.
- **View Movies**: View a list of all movies stored in the database.
- **Display Details**: Display detailed information about each movie, including title, rating, year of release, and poster image.
- **Dynamic Web Page**: The app generates a dynamic HTML page to show the list of movies.

## Project Structure
```
Movie-project/
├── fetch_data.py             # Refactor movie data storage: Replace JSON with SQL database and integrate API
├── movie_storage_sql.py      # Handle movie data storage and interaction with SQL database
├── templates/
│   └── index_template.html   # Template for the web page
├── .gitignore                # Exclude unnecessary files and sensitive information from version control
├── main.py                    # Main application logic
├── generate_html.py          # Generate dynamic HTML based on the movie data
├── final_movie.py            # Logic for adding, listing, and updating movies in the database
├── main.py                   # Entry point for running the application and user interaction
└── requirements.txt          # Python dependencies for the project
```



## Setup

To get the project up and running, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Movie-Mountain.git
cd Movie-Mountain
```
2. Set Up Virtual Environment
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. API Key Setup
Make sure you have a valid API key from the movie API provider.

Store your API key in a .env file in the root directory of the project:

```bash
API_KEY=your_api_key_here
```
5. Run the Application
```bash
python main.py
```
6. Open the Web Page
Once the application is running, visit movies.html to view the list of movies.

Functions
add_movie(title): Fetches movie data from the API based on the provided title and stores it in the database.

list_movies(): Retrieves and lists all movies stored in the SQLite database.

generate_html(): Generates an HTML page displaying all the movies.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Movie data is fetched from an external API. Make sure you get an API key for this to work.

The project uses SQLite for local database storage.

sql

