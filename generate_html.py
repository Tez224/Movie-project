import webbrowser
import os

def serialize_movies(movies):
    """
    Serializes the movies data into HTML format.
    :param movies: The movie dictionary to serialize.
    :return: The HTML representation of the movie.
    """
    output = ""
    for title, details in movies.items():
        output += "<li><div class='movie'>"
        output += f"<img class='movie-poster' src='{details['poster_url']}'/>"
        output += f"<div class='movie-title'>{title}</div>"
        output += f"<div class=movie-year>{details['rating']}</div></div></li>"

    return output


def generate_html(movies):
    """
    Generates the HTML content by replacing the placeholder with actual movie data.
    :return: The generated HTML content as a string.
    """
    html = get_html()
    movies_html_list = serialize_movies(movies)
    no_placeholder_content = "<p>No movie data html found.</p>"

    if movies_html_list:
        return html.replace("__TEMPLATE_MOVIE_GRID__", movies_html_list)
    else:
        print("Error: no html placeholder content got generated.")
        return html.replace("__TEMPLATE_MOVIE_GRID__", no_placeholder_content)


def get_html():
    """
    Reads the template HTML file and returns its content.
    :return: The template HTML content.
    """
    try:
        with open("templates/index_template.html", "r") as file:
            return file.read()
    except Exception as e:
        print(f"An error occurred while reading the template file: {e}")
        return ""


def write_html_to_file(movies):
    """
    Writes the generated HTML content to a file.
    html_content: The HTML content to write to the file.
    """
    html_content = generate_html(movies)

    try:
        with open("templates/movies.html", "w") as file:
            file.write(html_content)
        webbrowser.open(f"file://{os.path.realpath('templates/movies.html')}", new=2)
        print("HTML content has been written to movies.html")
    except Exception as e:
        print(f"Something went wrong while writing the HTML to the file: {e}")