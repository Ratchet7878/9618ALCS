class Character:
    def __init__(self, namep, xposp, yposp):
        self.__Name = namep
        self.__XPosition = xposp
        self.__YPosition = yposp

    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self, nxpos):
        self.__XPosition = nxpos
        if self.__XPosition > 10000:
            self.__XPosition = 10000
        if self.__XPosition < 0:
            self.__XPosition = 0

    def SetYPosition(self, nypos):
        self.__YPosition = nypos
        if self.__YPosition > 10000:
            self.__YPosition = 10000
        if self.__YPosition < 0:
            self.__YPosition = 0

    def Move(self, position):
        if position == "up":
            self.SetYPosition(10)
        if position == "down":
            self.SetYPosition(-10)
        if position == "right":
            self.SetXPosition(10)
        if position == "left":
            self.SetXPosition(-10)


Jack = Character("Jack", 50, 50)

class BikeCharacter(Character):
    def __init__(self, namep, xposp, yposp):
        super().__init__(namep, xposp, yposp)

    def Move(self, newpos):
        if newpos == "up":
            super().SetYPosition(20)
        if newpos == "down":
            super().SetYPosition(-20)
        if newpos == "right":
            super().SetXPosition(20)
        if newpos == "left":
            super().SetXPosition(-20)

Karla = BikeCharacter("Karla", 100, 50)

tomove = input("Which character to move? ")
todirection = input("Which direction to move: ")
if tomove == "jack":
    Jack.Move(todirection)
    newpositionX = Jack.GetXPosition()
    newpositionY = Jack.GetYPosition()
    print("Jack's new position is X = " + str(newpositionX) + " Y = " + str(newpositionY))
if tomove == "karla":
    Karla.Move(todirection)
    newpositionX = Karla.GetXPosition()
    newpositionY = Karla.GetYPosition()
    print("Karla's new position is X = " + str(newpositionX) + " Y = " + str(newpositionY))
