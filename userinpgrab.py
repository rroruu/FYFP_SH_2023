##user inputs taken
genre = ""
def userdata():
    global genre
    age = input("What is your age?: ")
    rhr = input("What is your resting heart rate?: ")
    genreind = input("\nAvailable Genres:\nPlease select your most preferred genre from the following...\n1. Pop 2. HipHop 3. Hardstyle\n")
    if genreind == 1:
        genre = "Pop"
    elif genreind == 2:
        genre = "HipHop"
    elif genreind == 3:
        genre = "Hardstyle"
    return genre
userdata()
print(genre)