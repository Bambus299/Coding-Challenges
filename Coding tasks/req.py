import requests
import os
def get_api_key():
    return os.environ.get("API_KEY")


def get_data(id : str) : 
    apikey = get_api_key()
    print(apikey)
    r = requests.get(f"https://codingchallenge.azurewebsites.net/api/riddle/{id}" , headers={"User-Token" : apikey} )
    return r.json()