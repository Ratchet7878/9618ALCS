class Card:
    def __init__(self, Numberp, Colourp):
        self.__Number = Numberp
        self.__Colour = Colourp

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

Cards = [] #array of record data type

file = open("CardValues.txt", "r")
for x in range(30):
    colornumber = int(file.readline().strip())
    colorname = file.readline().strip()
    Cards.append(Card(colornumber, colorname))

selectedcards = [False] * 30
def ChooseCard():
    global selectedcards
    flag = True
    while flag:
        CardSelected = int(input("Enter an integer: "))
        if CardSelected < 1 or CardSelected > 30:
            CardSelected = int(input("Enter an integer: "))
        elif selectedcards[CardSelected - 1] == True:
            print("Not available")
        else:
            print("Valid")
            flag = False

    selectedcards[CardSelected - 1] = True
    return CardSelected - 1

Player1 = [] # array of 4 cards
for x in range(4):
    ReturnValue = ChooseCard()
    Player1.append(Cards[ReturnValue])

for x in range(4):
    print(Player1[x].GetNumber())
    print(Player1[x].GetColour())

