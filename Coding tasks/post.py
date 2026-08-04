import requests
import os

def get_api_key():
    return os.environ.get("API_KEY")


def post_data(id : str, data : dict) : 
    apikey = get_api_key()
    print(apikey)
    r = requests.post(f"https://codingchallenge.azurewebsites.net/api/solution/{id}" , headers={"User-Token" : apikey, "Content-Type" : "application/json"},json=data )
    return r.json()