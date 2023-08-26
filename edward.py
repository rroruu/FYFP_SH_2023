import requests

resp = requests.post("https://accounts.spotify.com/api/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, params={"grant_type": "client_credentials", "client_id": "18646cd687534f62be82b2492d7e379a", "client_secret": "7215f1ff173f4752b928534fd8c6f121"})
resp = resp.json()['access_token']

# Make a simple request
BASE_URL = "https://api.spotify.com"
headers = {
    "Authorization": f"Bearer {resp}"
}

track_id = "5ubvP9oKmxLUVq506fgLhk"

response = requests.get(BASE_URL + "/v1/audio-features/" + track_id, headers=headers)

# print(response.json())

# print(response.json()['tempo'])

response = requests.get(BASE_URL + "/v1/audio-features/", params={"ids": "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"}, headers=headers)

print(response.json()['audio_features'][1])


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
