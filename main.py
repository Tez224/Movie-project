from final_movie import colors, choose_menu
import movie_storage_sql as storage


def main():
    """Entry point of the program. Initializes the movie database and starts the menu loop."""
    print(colors['title'] + "********** My Movies Database **********" + "\n")
    movies = storage.list_movies()
    choose_menu(movies)


if __name__ == "__main__":
    main()