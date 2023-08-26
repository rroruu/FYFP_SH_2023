##user inputs taken
genre = ""
maxrate = ""
allgenres = ["pop", "hiphop", "hardstyle"]
def userdata():
    global genre
    global maxrate
    age = int(input("What is your age?: "))
    rhr = int(input("What is your resting heart rate? (BPM): "))
    genreind = int(input("\nAvailable Genres:\nPlease select your most preferred genre from the following...\n1. Pop 2. HipHop 3. Hardstyle\n"))

    genre = allgenres[genreind-1]
    maxrate = str(220 - age)
    return genre, maxrate
    
userdata()
print("\nYour preferred genre is "+str(genre)+"!")
print("Your calculated maximum heart rate (BPM) is "+maxrate+" bpm.")