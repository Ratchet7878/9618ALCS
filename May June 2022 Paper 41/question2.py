class Balloon:
    def __init__(self, Defencep, Colourp):
        self.__Health = 100
        self.__Colour = Colourp
        self.__DefenceItem = Defencep

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, InNum):
        self.__Health = InNum + self.__Health

    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False

DefenceMethod = input("Enter Defence Method: ")
ColourBalloon = input("Enter the colour of your juicy balloons: ")
Balloon1 = Balloon(DefenceMethod, ColourBalloon)

def Defend(BalloonObject):
    opponentstrength = int(input("How strong is the opponent? "))
    BalloonObject.ChangeHealth(-opponentstrength)
    print("The defence item is " + str(BalloonObject.GetDefenceItem()))
    healthstatus = BalloonObject.CheckHealth()
    if healthstatus:
        print("No health left")
    else:
        print("Baby you are strong!")
    return BalloonObject

x = Defend(Balloon1)


