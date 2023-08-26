from flask import Flask, render_template, request, redirect
import requests
import math

'''
Import Flask framework for building web app
Import render_template for rendering HTML templates
Import request for accessing incoming HTTP request data
Import redirect for URL redirection
Import requests for making HTTP requests to Spotify API
'''

def get_token():
    # Data for requesting the access token - sends POST request to spotify API
    data = {
         #From Jess' spotify dev acc
        'grant_type': 'client_credentials',
        'client_id': '4a7eed16649645f198e0e08948805619',
        'client_secret': 'b42f853c09ac488fa8b0df72628019a9',
    }
    response = requests.post('https://accounts.spotify.com/api/token', data=data)
    return response.json()['access_token']
headers = {
    'Authorization': f'Bearer {get_token()}',
}   

def get_closest_song(heart_rate, playlist_id):
    playlist = requests.get('https://api.spotify.com/v1/playlists/' + playlist_id, headers=headers).json()
    song_ids = [song['track']['id'] for song in playlist['tracks']['items']]

    params = {
        'ids': ','.join(song_ids)
    }

    response = requests.get('https://api.spotify.com/v1/audio-features', params=params, headers=headers)
    song_features = response.json()['audio_features']
    song_tempo_list = [(song["tempo"], song["id"]) for song in song_features]

    song_tempo_list.sort()
    closest_value = 0
    smallest_distance = math.inf

    for (tempo, id) in song_tempo_list:
        distance = abs(tempo - heart_rate)
        if distance < smallest_distance:
            closest_id = id
            smallest_distance = distance
        else:
            break

    return closest_id

# Create a Flask app instance
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def main():
    title = "Tempo.fy"
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    return render_template('index.html', id=get_closest_song(float(request.form['bpm']), request.form['playlist'].split("/")[-1]))

app.run()