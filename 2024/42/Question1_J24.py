WordArray = []
NumberWords = 0

def Play():
    global WordArray, NumberWords
    length_array = len(WordArray)
    got_Correct = 0
    main_word = WordArray[0]
    print("The main word is: ", main_word)
    print("The number of answers: ", NumberWords)
    userAnswer = input('Enter your answer or enter "no" to stop: ')
    while userAnswer != "no":
        count = 0
        success = False
        while not success and count < length_array:
            for x in range(1, length_array):
                if userAnswer == WordArray[x]:
                    print("It is an answer")
                    WordArray[x] = ""
                    got_Correct += 1
                    userAnswer = input('Enter your answer or enter "no" to stop: ')
                    success = True
                    break
                count += 1
        if not success:
            print("This is not an answer")
            userAnswer = input('Enter your answer or enter "no" to stop: ')
    precentage_Correct = int((got_Correct/NumberWords) * 100)
    print("The percentage of correct answers is: ", precentage_Correct, "%")
    for x in range(length_array):
        if WordArray[x] != "":
            print(WordArray[x])


def ReadWords(FileName):
    global WordArray, NumberWords
    try:
        file = open(FileName, "r")
        file_data = file.readline().strip()
        while file_data != "":
            WordArray.append(file_data)
            NumberWords += 1
            file_data = file.readline().strip()
        NumberWords = NumberWords - 1
        file.close()
        Play()
    except IOError:
        print("File not found")

userChoice = input('Enter "easy", "medium", or "hard" to play: ')
if userChoice == "easy":
    ReadWords("Easy.txt")
elif userChoice == "medium":
    ReadWords("Medium.txt")
elif userChoice == "hard":
    ReadWords("Hard.txt")
else:
    print("Invalid Input")

