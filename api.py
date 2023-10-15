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
    return {"Authorization": f"Bearer {token}"}



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
    


def get_songs(token):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    params = { 
        "q": "genre:rock",
        "type": "track",
        "limit": 10
    }

    result  =  get(url, headers=headers, params=params)

    if result.status_code == 200:
        json_result  = json.loads(result.content)
        return json_result
    

def clear_json_file():
    try:
        with open("dataset.json", "w") as file:
            pass
    except FileNotFoundError:
        print("file was not found")



def check_json_file(data):
    try:
        with open("dataset.json", "r") as file:
            if file == 0:
                with open("dataset.json", "w") as files:
                   json.dump(data, files)
            else:
                clear_json_file()
    except FileNotFoundError:
        print("file not found")



def data_function_artisttracks():
    tokens = get_token()
    artist_data = search_for_artist(tokens, "davido")
    artist_id = artist_data
    tracks = get_artist_song(tokens, artist_id)
    
    check_json_file(tracks)

    return tracks



# this function create the 
def create_playlis(token):
    playlistname = ""
    playlist_description = ""

    url = "https://api.spotify.com/v1/me/playlists"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    params = {
        "name": playlistname,
        "description": playlist_description,
        "public": True
    }
    
    result = get(url, headers=headers, params=params)

    if result.status_code == 201:
        pass


def data_function_searchmusic():
    token = get_token()
    search = get_songs()

token = get_token()

result = get_songs(token)
print(result)






