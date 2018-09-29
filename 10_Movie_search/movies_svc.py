import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')


def find_movies(search_keyword):

    if not search_keyword or not search_keyword.strip():
        raise ValueError("Search term required!")

    url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search_keyword)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    movies.sort(key=lambda m: -m.year)  # minus sorts descending

    return movies

