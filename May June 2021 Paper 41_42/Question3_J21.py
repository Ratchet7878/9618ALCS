class TreasureChest:
    def __init__(self, questionp, answerp, pointsp):
        self.__question = questionp
        self.__answer = answerp
        self.__points = pointsp
    
    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, useranswer):
        if useranswer == self.__answer:
            return True
        else:
            return False
    
    def getPoints(self, numberofattempts):
        if numberofattempts == 1:
            return self.__points
        elif numberofattempts == 2:
            newpoints = (self.__points) // 2
            return newpoints
        elif numberofattempts == 3 or numberofattempts == 4:
            newpoints = (self.__points) // 2
            return newpoints
        else:
            return 0   

arrayTreasure = [] #array of type TreasureChest
def readData():
    global arrayTreasure

    try:
        file = open("TreasureChestData.txt", "r")
        for x in range(5):
            question = file.readline().strip()
            answer = file.readline().strip()
            points = file.readline().strip()
            arrayTreasure.append(TreasureChest(question, answer, points))
    except FileNotFoundError:
        print("The file is not found!")

readData()
questionnum = int(input("Enter a question number between 1 to 5: "))
questionnum = questionnum - 1
question = arrayTreasure[questionnum].getQuestion()
print(question)
answer = input("Please enter the answer: ")
numberofattemps = 0
correct = False
while not correct:
    correct = arrayTreasure[questionnum].checkAnswer(answer)
    numberofattemps += 1
score = arrayTreasure[questionnum].getPoints(numberofattemps)
print(score)
               