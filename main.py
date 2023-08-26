import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = '23ae51f0229648a48c2a5dedcda3af39'
CLIENT_SECRET = '37127deb51da4d568e9703268c460969'
REDIRECT_URI = 'http://localhost:8080/callback'
'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope='user-modify-playback-state'))

def control_playback(device_id, action):
    if action == 'play':
        sp.start_playback(device_id=device_id)
    elif action == 'pause':
        sp.pause_playback(device_id=device_id)
    elif action == 'next':
        sp.next_track(device_id=device_id)
    elif action == 'previous':
        sp.previous_track(device_id=device_id)
    else:
        print("Unknown action")
        return

if __name__ == "__main__":
    devices = sp.devices()
    
    if devices['devices']:
        device_id = devices['devices'][0]['id']  # Use the first available device
        action = input("Enter action (play/pause/next/previous): ")
        control_playback(device_id, action)
    else:
        print("No active devices found.")
