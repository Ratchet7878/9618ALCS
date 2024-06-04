class Card:
    def __init__(self, Numberp, Colourp):
        #PRIVATE Number : STRING
        #PRIVATE Colour : STRING
        self.__Number = Numberp
        self.__Colour = Colourp

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

FirstRed = Card(1, "red")
SecondRed = Card(2, "red")
ThirdRed = Card(3, "red")
FourthRed = Card(4, "red")

FirstBlue = Card(1, "blue")
SecondBlue = Card(2, "blue")
ThirdBlue = Card(3, "blue")
FourthBlue = Card(4, "blue")

FirstYellow = Card(1, "yellow")
SecondYellow = Card(2, "yellow")
ThirdYellow = Card(3, "yellow")
FourthYellow = Card(4, "yellow")
FifthYellow = Card(5, "yellow")

class Hand:
    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__FirstCard = 0
        self.__NumberCards = 5
        self.__Cards = []
        self.__Cards.append(Card1)
        self.__Cards.append(Card2)
        self.__Cards.append(Card3)
        self.__Cards.append(Card4)
        self.__Cards.append(Card5)


    def GetCard(self, cardNum):
        return self.__Cards[cardNum]

Player1 = Hand(FirstRed, SecondRed, ThirdRed, FourthRed, FirstYellow)
Player2 = Hand(SecondYellow, ThirdYellow, FourthYellow, FifthYellow, FirstBlue)

def CalculateValue(Player):
    Score = 0
    for count in range(0, 4):
        playercard = Player.GetCard(count) #gets the player hand
        Score = Score + playercard.GetNumber()
        Colour = playercard.GetColour()
        if Colour == "red":
            Score = Score + 5
        elif Colour == "blue":
            Score = Score + 10
        else:
            Score = Score + 15
    return Score

Player1Score = CalculateValue(Player1)
Player2Score = CalculateValue(Player2)
if Player1Score > Player2Score:
    print("Player 1 wins.")
elif Player1Score < Player2Score:
    print("Player 2 wins.")
else:
    print("It is a draw.")

