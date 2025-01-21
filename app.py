from flask import Flask, request, jsonify, render_template
from flask_session import Session
from flask_cors import CORS
import os
from dotenv import load_dotenv
from requests import post, get
import json
import base64

from functionality import get_artist

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

app = Flask(__name__)
CORS(app)

# Configure Flask-Session
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in files (use Redis for production)
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/help.html')
def help():
    return render_template('help.html')


@app.route('/submit', methods=['POST'])
def guess_word():
    data = request.get_json()
    print(data)
    artist_name = get_artist(data)  # Ensure key is passed in the request
    token = get_token()  # Get Spotify token

    if token:
        print("OK IM SEARCHING")
        artist = search_artist(token, artist_name)  # Search for the artist using the token
        print("RETURNING\n", artist)
        return jsonify({"message": artist})
    else:
        print("DIDNT MAKE SPOTIFY CALL NO TOKEN")
        return jsonify({"message": "Error: Unable to retrieve the token"}), 400


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data)

    # Check the response status code
    if result.status_code == 200:
        json_result = result.json()
        token = json_result["access_token"]
        return token
    else:
        print("Error: Unable to retrieve the token")
        return None
    

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    print("FUCKFUCKFUCKFUCK")

    if result.status_code == 200:
        json_result = result.json()
        artist = json_result["artists"]["items"][0] if json_result["artists"]["items"] else None
        print(artist)
        if artist:
            return artist
        else:
            print("artist found 1")
            return {"error": "Artist not found"}
    else:
        print("bad api call")
        return {"error": f"Error searching artist: {result.status_code}, {result.text}"}


if __name__ == '__main__':
    app.run(debug=True, port=8080)
