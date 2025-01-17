HighScores = [[''] * 3 for x in range(7) for y in range(7)]

def ReadData():
    try:
        file = open("HighScoreTable.txt", "r")
        for x in range(7):
            PlayerID = file.readline().strip()
            GameLevel = file.readline().strip()
            Score = file.readline().strip()
            HighScores[x][0] = PlayerID
            HighScores[x][1] = GameLevel
            HighScores[x][2] = Score
        return HighScores
        file.close()
    except FileNotFoundError:
        print("The file was not found")

def OutputHighScores(HighScores):
    for x in range(7):
        print(HighScores[x][0], " reached level ", HighScores[x][1], " with a score of ", HighScores[x][2])

def SortArrays(HighScores):
    lenArray = len(HighScores)
    for x in range(lenArray - 1):
        for y in range(lenArray - x - 1):
            if HighScores[y][1] < HighScores[y + 1][1]:
                HighScores[y][1], HighScores[y + 1][1] = HighScores[y + 1][1], HighScores[y][1]
            elif HighScores[y][1] == HighScores[y][1]:
                if HighScores[y][2] < HighScores[y+ 1][2]:
                   HighScores[y][2], HighScores[y + 1][2] = HighScores[y + 1][2], HighScores[y][2]
    return HighScores

unsorted_array = ReadData()
print("Before")
OutputHighScores(unsorted_array)
sorted = SortArrays(unsorted_array)
print("After")
OutputHighScores(sorted)


