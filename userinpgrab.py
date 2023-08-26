##user inputs taken
import requests

def userdata():
    PlaylistID = input("Which playlist URL would you like to play from? ")
    #gets playlist name from playlist ID
    PlaylistName = spotify.user_playlist(user=None, playlist_id="3cqDkXVInhOYPpJyVzvwux", fields="name")
    PlaylistName["name"]
    HeartRate = int(input("What is your resting heart rate? (BPM): "))
    return HeartRate, PlaylistName
    
userdata()
print(HeartRate)
print(PlaylistName)
print(PlaylistID)

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