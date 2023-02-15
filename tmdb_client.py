import json
import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmN2Q2NDNlMDlhNWIwY2I3MmY3ZjZhNTFiMmFjYWEwMSIsInN1YiI6IjYzZWNjYWUwOGU4NzAyMDA3YTFhOWJlNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.39WT6XqB8xd_Nladee7HLsHllkAm6YuUtMx9cXHEd8M"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]