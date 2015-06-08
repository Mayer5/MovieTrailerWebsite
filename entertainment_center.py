__author__ = 'Mayer'

import json
import media
import fresh_tomatoes


def load_json_info(json_file):
    """
    :param json_file: string name of the json file
    :return: the data in json format
    """
    with open(json_file) as data_file:
        data = json.load(data_file)
    return data


def generate_movie_lists(json_file="movies.json"):
    """
    :param json_file: string name of the json file which contains movies' info
    :return: a list contain movies' information
    """
    movies = []
    movies_info = load_json_info(json_file)
    for movie_value in movies_info.values():
        movies.append(media.Movie(movie_value["title"], movie_value["image"], movie_value["url"], movie_value["storyline"]))
    return movies

if __name__ == '__main__':
    movies_list = generate_movie_lists()
    # generate a list which contains movies info
    fresh_tomatoes.open_movies_page(movies_list)
    # use fresh_tomatoes to generate the website