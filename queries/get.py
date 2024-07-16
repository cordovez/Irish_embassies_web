import requests


def get_all(url):
    response = requests.get(url)
    return response.json()
