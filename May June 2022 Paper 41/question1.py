PlayerArray = [[''] * 2 for x in range(11)]

def ReadHighScores():
    global PlayerArray
    try:
        file = open("HighScore.txt", "r")
        #reads the first player name
        filedata = file.readline().strip()
        counter = 0
        while filedata != "":
            PlayerArray[counter][0] = filedata
            filedata = file.readline().strip()
            PlayerArray[counter][1] = filedata
            counter += 1
            #reads a new player name
            filedata = file.readline().strip()
        file.close()
    except IOError:
        print("File not found")

print("Before:")
def OutputHighScores():
    for x in range(11):
        print(PlayerArray[x][0] + " " + str(PlayerArray[x][1]))

ReadHighScores()
OutputHighScores()

newuser = input("Enter 3 character palyer: ")
newscore = int(input("Enter score between 1 and 10000: "))

def NewPlayerCreation(newuser, newscore):
    global PlayerArray
    if newscore < 1 or newscore > 100000:
        print("Format is invalid")
    else:
        #places the new data
        for x in range(11):
            if PlayerArray[x][0] == "":
                PlayerArray[x][0] = newuser
                PlayerArray[x][1] = newscore
        #sorting the array in descending order using insertion sort
        for x in range(1, 11):
            TempPlayer = PlayerArray[x][0]
            TempScore = PlayerArray[x][1]
            TempPointer = x
            while TempPointer > 0 and int(PlayerArray[TempPointer - 1][1]) < int(TempScore):
                PlayerArray[TempPointer][0] = PlayerArray[TempPointer - 1][0]
                PlayerArray[TempPointer][1] = PlayerArray[TempPointer - 1][1]
                TempPointer -= 1
            PlayerArray[TempPointer][0] = TempPlayer
            PlayerArray[TempPointer][1] = TempScore


NewPlayerCreation(newuser, newscore)
print("After")
OutputHighScores()

def WriteTopTen():
    global PlayerArray
    file = open("NewHighScore.txt", "w")
    for x in range(11):
        filedata = PlayerArray[x][0]
        #uses '\n' for adding the data in a new line
        file.write(str(filedata) + '\n')
        filedata = PlayerArray[x][1]
        file.write(str(filedata) + '\n')
    file.close()

WriteTopTen()