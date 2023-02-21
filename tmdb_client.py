import json
import requests

api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmN2Q2NDNlMDlhNWIwY2I3MmY3ZjZhNTFiMmFjYWEwMSIsInN1YiI6IjYzZWNjYWUwOGU4NzAyMDA3YTFhOWJlNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.39WT6XqB8xd_Nladee7HLsHllkAm6YuUtMx9cXHEd8M'
api_key = 'f7d643e09a5b0cb72f7f6a51b2acaa01'


def get_poster_url(poster_api_path, size="w342"):
    base_url = 'https://image.tmdb.org/t/p/'
    return f'{base_url}{size}/{poster_api_path}'


def get_popular_movies(list_type):
    endpoint = f'https://api.themoviedb.org/3/movie/{list_type}'
    headers = {
        "Authorization": f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies(how_many, list_type):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}'
    headers = {
        "Authorization": f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
    headers = {
        "Authorization": f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movies_list(list_type):
    endpoint = f'https://api.themoviedb.org/3/movie/{list_type}'
    headers = {
        "Authorization": f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def search(search_query):
    endpoint = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={search_query}'
    response = requests.get(endpoint)
    response = response.json()
    return response['results']


def get_airing_today():
    endpoint = f'https://api.themoviedb.org/3/tv/airing_today'
    headers = {
        "Authorization": f'Bearer {api_token}'
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']
