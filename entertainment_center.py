__author__ = 'Mayer'

import json
import media
import fresh_tomatoes


def load_json_info(json_file):
    with open(json_file) as data_file:
        data = json.load(data_file)
    return data


def generate_movie_lists(json_file="movies.json"):
    movies = []
    movies_info = load_json_info(json_file)
    for movie_value in movies_info.values():
        movies.append(media.Movie(movie_value["title"], movie_value["image"], movie_value["url"]))
    return movies

if __name__ == '__main__':
    movies_list = generate_movie_lists()
    fresh_tomatoes.open_movies_page(movies_list)