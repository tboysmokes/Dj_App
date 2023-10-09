import base64
from dotenv import load_dotenv
from requests import post, get
import json
import os

load_dotenv()

client_Id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
print(client_Id, client_secret)


def get_token():
    auth_string = client_Id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "basic" + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    Gettoken = post(url, headers=headers, data=data)

    if Gettoken.status_code == 200:
        tokene = json.loads(Gettoken.content)
        token = tokene["access_token"]
        return token
    else:
        print(f"Error: {Gettoken.status_code}-{Gettoken.text}")

tokens = get_token()
print(tokens)
