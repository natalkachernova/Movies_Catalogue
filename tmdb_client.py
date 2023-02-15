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
