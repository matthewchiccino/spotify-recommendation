from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
from flask_cors import CORS
from dotenv import load_dotenv
from requests import post, get
import base64
import os
import yaml

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

app = Flask(__name__)
CORS(app)

# Configure Flask-Session
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in files
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

with open('artist_data.yaml', 'r') as file:
    artist_data = yaml.safe_load(file)

def convert_to_tuple_key_mapping(artist_list):
    mapping = {}
    for item in artist_list:
        key_tuple = tuple(item['key'])
        mapping[key_tuple] = item['value']
    return mapping

rap_artist_mappings = convert_to_tuple_key_mapping(artist_data['rap_artist_mappings'])
rock_artist_mappings = convert_to_tuple_key_mapping(artist_data['rock_artist_mappings'])
pop_artist_mappings = convert_to_tuple_key_mapping(artist_data['pop_artist_mappings'])
varied_artist_mappings = convert_to_tuple_key_mapping(artist_data['varied_artist_mappings'])


def get_artist(answers):
    if answers['6'] == "rap":
        artist_id = rap_artist_mappings[tuple(answers.values())]
    elif answers['6'] == "pop":
        del answers["1"]
        del answers["6"]
        artist_id = pop_artist_mappings[tuple(answers.values())]
    elif answers['6'] == "rock":
        del answers["1"]
        del answers["6"]
        artist_id = rock_artist_mappings[tuple(answers.values())]
    else:
        del answers["1"]
        del answers["6"]
        artist_id = varied_artist_mappings[tuple(answers.values())]

    print("IM SEARCHING FOR", artist_id)

    return artist_id


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)

    if result.status_code == 200:
        json_result = result.json()
        artist = json_result["artists"]["items"][0] if json_result["artists"]["items"] else None
        print(artist)
        if artist:
            return artist
        else:
            return {"error": "Artist not found"}
    else:
        return {"error": f"Error searching artist: {result.status_code}, {result.text}"}

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
    session['data'] = request.get_json()
    print("answers", session['data'])
    session['artist_name'] = get_artist(session['data'])  # Ensure key is passed in the request
    token = get_token()  # Get Spotify token

    if token:
        print("searching for artist")
        session['artist'] = search_artist(token, session['artist_name'])  # Search for the artist using the token
        print("returning\n", session['artist'])
        return jsonify({"message": session['artist']})
    else:
        print("Unable to retrieve the token")
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

"""
# local host for development
if __name__ == '__main__':
    app.run(debug=True, port=8080)
"""