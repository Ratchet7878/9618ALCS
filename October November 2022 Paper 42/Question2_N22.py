class Character:
    def __init__(self, Namep, XCoordinatep, YCoordinatep):
        self.__Name = Namep
        self.__XCoordinate = XCoordinatep
        self.__YCoordinate = YCoordinatep
    
    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange
    

Characters = [] #Of character type
try:
    file = open("Characters.txt", "r")
    for x in range(10):
        name = file.readline().strip()
        x_coordinate = file.readline().strip()
        y_coordinate = file.readline().strip()
        Characters.append(Character(name, int(x_coordinate), int(y_coordinate)))
    file.close()
except FileNotFoundError:
    print("File not found!")


index_posn = -1
while (index_posn == -1):
    userinput = input("Enter a valid name: ").lower()
    for x in range(10):
        temp = str(Characters[x].GetName())
        if userinput == temp.lower():
            index_posn = x

to_move = input("Enter letters A, W, S or D: ")
correct = False
while not correct:
    if to_move == "A" or to_move == "W" or to_move == "S" or to_move == "D":
        correct = True
    else:
        to_move = input("Enter letters A, W, S or D: ")
if to_move == "A":
    Characters[index_posn].ChangePosition(-1, 0)
elif to_move == "W":
    Characters[index_posn].ChangePosition(0, 1)
elif to_move == "S":
    Characters[index_posn].ChangePosition(0, -1)
else:
    Characters[index_posn].ChangePosition(1, 0)

print((Characters[index_posn].GetName()), " has changed coordinates to X = ", str(Characters[index_posn].GetX()), " and Y = ", str(Characters[index_posn].GetY()))
