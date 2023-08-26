import requests
# Make a simple request
BASE_URL = "https://api.spotify.com"
headers = {
    "Authorization": "Bearer BQDTlaKNeRhN09uTN0iv4r7grdg966RkqnGZk16ghrlrMBvFURSgP87R8q-3abf9vR8-xDGSdUPi9ikHAFgdF4eFJirFGelj7a_25Z_jDi1Uce0YiqU"
}

track_id = "5ubvP9oKmxLUVq506fgLhk"

response = requests.get(BASE_URL + "/v1/audio-features/" + track_id, headers=headers)
"BQDTlaKNeRhN09uTN0iv4r7grdg966RkqnGZk16ghrlrMBvFURSgP87R8q-3abf9vR8-xDGSdUPi9ikHAFgdF4eFJirFGelj7a_25Z_jDi1Uce0YiqU"

print(response.json()['tempo'])

response = requests.get(BASE_URL + "/v1/audio-features/", params={"ids": "id1,id2,id3"}, headers=headers)
"BQDTlaKNeRhN09uTN0iv4r7grdg966RkqnGZk16ghrlrMBvFURSgP87R8q-3abf9vR8-xDGSdUPi9ikHAFgdF4eFJirFGelj7a_25Z_jDi1Uce0YiqU"