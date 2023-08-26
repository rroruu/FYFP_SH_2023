##user inputs taken
import requests
from pprint import pprint
import math

def userdata():
    PlaylistID = "7dS7DSLcNQjRf9jwjL5pLu"
    response = requests.get('https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n', headers=headers)
    HeartRate = int(input("What is your resting heart rate? (BPM): "))
    return HeartRate, response
    
def get_token():
    data = {
        'grant_type': 'client_credentials',
        'client_id': '4a7eed16649645f198e0e08948805619',
        'client_secret': 'b42f853c09ac488fa8b0df72628019a9',
    }
    response = requests.post('https://accounts.spotify.com/api/token', data=data)
    return response.json()['access_token']
headers = {
    'Authorization': f'Bearer {get_token()}',
}

heart_rate, response = userdata()
print(heart_rate)
data = response.json()
print(data["name"])


song_ids = [song['track']['id'] for song in data['tracks']['items']]

params = {
    'ids': ','.join(song_ids)
}

response = requests.get('https://api.spotify.com/v1/audio-features', params=params, headers=headers)
song_features = response.json()['audio_features']
song_tempo_list = [(song["tempo"], song["id"]) for song in song_features]
pprint(song_tempo_list)

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

print(closest_id)



##song_tempos = requests.get('https://api.spotify.com/v1/audio-features/'+song['track']['id']['tempo'])

#data['tracks']['items'] is all songs
#resp = requests.post("https://accounts.spotify.com/api/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, params={"grant_type": "client_credentials", "client_id": "18646cd687534f62be82b2492d7e379a", "client_secret": "7215f1ff173f4752b928534fd8c6f121"})
#print(resp.json())

#input bpm
#input url of playlist
#iterate through each song in playlist
#call the bpm of each song and store
#find closest matching bpm

#html flask

#match closest to bpm
#get track id and embed spotify track in site

#some faking is alright
#generic UI html, css, javascript