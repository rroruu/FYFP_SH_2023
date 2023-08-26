import requests

resp = requests.post("https://accounts.spotify.com/api/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, params={"grant_type": "client_credentials", "client_id": "18646cd687534f62be82b2492d7e379a", "client_secret": "7215f1ff173f4752b928534fd8c6f121"})


# Make a simple request
BASE_URL = "https://api.spotify.com"
headers = {
    "Authorization": "Bearer BQDTlaKNeRhN09uTN0iv4r7grdg966RkqnGZk16ghrlrMBvFURSgP87R8q-3abf9vR8-xDGSdUPi9ikHAFgdF4eFJirFGelj7a_25Z_jDi1Uce0YiqU"
}

track_id = "5ubvP9oKmxLUVq506fgLhk"

response = requests.get(BASE_URL + "/v1/audio-features/" + track_id, headers=headers)
"BQDTlaKNeRhN09uTN0iv4r7grdg966RkqnGZk16ghrlrMBvFURSgP87R8q-3abf9vR8-xDGSdUPi9ikHAFgdF4eFJirFGelj7a_25Z_jDi1Uce0YiqU"

print(response.json())

print(response.json()['tempo'])

response = requests.get(BASE_URL + "/v1/audio-features/", params={"ids": "id1,id2,id3"}, headers=headers)
"BQDTlaKNeRhN09uTN0iv4r7grdg966RkqnGZk16ghrlrMBvFURSgP87R8q-3abf9vR8-xDGSdUPi9ikHAFgdF4eFJirFGelj7a_25Z_jDi1Uce0YiqU"


# def main():
#     while True:
#         heart_rate = input("Input a heart rate value in integers: ")
#         try:
#             heart_rate = int(heart_rate.strip())
#             if heart_rate == 0:
#                 return





#         except:
#             print("Wrong bruh.")


# if __name__ == '__main__':
#     main()
