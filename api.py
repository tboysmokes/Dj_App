import base64
from dotenv import load_dotenv
from requests import post, get
import json
import os

load_dotenv()

client_Id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_Id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}

    Gettoken = post(url, headers=headers, data=data)
    
# error managment 
    if Gettoken.status_code == 200:
        tokene = json.loads(Gettoken.content)
        token = tokene["access_token"]
        return token
    else:
        print(f"Error: {Gettoken.status_code}-{Gettoken.text} this is the problem")


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}



def search_for_artist(tokens, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(tokens)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    request = get(query_url, headers=headers)

    if request.status_code == 200:
        json_result = json.loads(request.content)
        artist_data = json_result['artists']['items']

        if len(artist_data) == 0:
            return f"{request.status_code} for the get_artist_id function"
        else:
            return artist_data[0]['id']
    else:
        return f"{request.status_code} for the get_artist_id function"


def get_artist_song(tokens, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US"
    headers = get_auth_header(tokens)
    request = get(url, headers=headers)

    if request.status_code == 200:
        json_result = json.loads(request.content)
        artist_tracks = json_result["tracks"]

        return artist_tracks
    
    else:
        return f"{request.status_code} for the get_artist_song function"
    


    




     


tokens = get_token()
artist_data = search_for_artist(tokens, "davido")
artist_id = artist_data
print(artist_id)
tracks = get_artist_song(tokens, artist_id)
print(tracks)

with open("dataset.json", "w") as json_file:
    json.dump(tracks, json_file)