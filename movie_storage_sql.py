from sqlalchemy import create_engine, text

# Define the database URL
DB_URL = "sqlite:///movies.db"
engine = create_engine(DB_URL, echo=True)   # Create the engine

def create_database():
    """ Creates the database for storing the movies. """
    # Create the movies table if it does not exist
    with engine.connect() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                year INTEGER NOT NULL,
                rating REAL NOT NULL,
                poster_url TEXT NOT NULL
            )
        """))
        connection.commit()


def list_movies():
    """Retrieve all movies from the database."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT title, year, rating FROM movies"))
        movies = result.fetchall()

    return {row[0]: {"year": row[1], "rating": row[2]} for row in movies}


def add_movie(title, year, rating, poster_url):
    """Add a new movie to the database."""
    try:
        with engine.connect() as connection:
            # Use the execute method to run the query, passing the parameters as a dictionary
            connection.execute(text("INSERT INTO movies (title, year, rating, poster_url) VALUES (:title, :year, :rating, :poster_url)"),
                               {"title": title, "year": year, "rating": rating, "poster_url": poster_url})

            connection.commit()
            print(f"Movie '{title}' added successfully.")
    except Exception as e:
        print(f"Error: {e}")


def delete_movie(title):
    """Delete a movie from the database."""
    with (engine.connect() as connection):
        try:
            connection.execute(text("DELETE FROM movies WHERE title = :title;"),
                               {"title": title})
            connection.commit()
            print(f"Movie '{title}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting movie: {e}")


def update_movie(title, rating):
    """Update a movie's rating in the database."""
    with (engine.connect() as connection):
        try:
            connection.execute(text(f"UPDATE movies SET rating = :rating WHERE title = :title;"),
                               {"rating": rating, "title": title})
            connection.commit()
            print(f"Movie {title} successfully updated to rating: {rating}")
        except Exception as e:
            print(f"Error while updating '{title}': {e}")