import json

movie_dict ={
            "The Shawshank Redemption": {
                "Rating": 9.5, "Year": 1994
            },
            "Pulp Fiction": {
                "Rating": 3.6, "Year": 1994
            },
            "The Room": {
                "Rating": 3.6, "Year": 2003
            },
            "The Godfather":{
                "Rating": 9.2, "Year": 1972
            },
            "The Godfather: Part II": {
                "Rating": 9.0, "Year": 1974
            },
            "The Dark Knight": {
                "Rating": 9.0, "Year": 2008
            },
            "12 Angry Men": {
                "Rating": 8.9, "Year": 1957
            },
            "Everything Everywhere All At Once": {
                "Rating": 8.9, "Year": 2022
            },
            "Forrest Gump": {
                "Rating": 8.8, "Year": 1994
            },
            "Star Wars: Episode V": {
                "Rating": 8.7, "Year": 1980
            }

}


json_str = json.dumps(movie_dict)
with open("movie_file.json", "w") as fileobj:
    fileobj.write(json_str)

