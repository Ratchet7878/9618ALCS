class Horse:
    def __init__(self, Namep, MaxFenceHeightp, PercentageSuccessp):
        self.__Name = Namep
        self.__MaxFenceHeight = MaxFenceHeightp
        self.__PercentageSuccess = PercentageSuccessp
    
    def GetName(self):
        return self.__Name
    
    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight
    
    def Success(self, height, risk):
        if self.__MaxFenceHeight < height:
            return self.__PercentageSuccess * 0.2 * 100
        else:
            if risk == 5:
                return self.__PercentageSuccess * 0.6 * 100
            elif risk == 4:
                 return self.__PercentageSuccess * 0.7 * 100
            elif risk == 3:
                 return self.__PercentageSuccess * 0.8 * 100
            elif risk == 2:
                 return self.__PercentageSuccess * 0.9 * 100
            elif risk == 1:
                return self.__PercentageSuccess * 100
    
class Fence:
    def __init__(self, Heightp, Riskp):
        self.__Height = Heightp
        self.__Risk = Riskp
    
    def GetHeight(self):
        return self.__Height
    
    def GetRisk(self):
        return self.__Risk
    

Horses = []
Horses.append(Horse("Beauty", 150, 0.72))
Horses.append(Horse("Jet", 160, 0.65))

print(Horses[0].GetName())
print(Horses[1].GetName())


Course = []
for i in range(4):
    while True:
        height = int(input("Enter height "))
        risk = int(input("Enter the risk value "))
        if (height >= 70 and height <= 180) and (risk >= 1 and risk <= 5):
            break
    Course.append(Fence(height, risk))

total1 = 0
total2 = 0
for i in range(4):
    chance = Horses[0].Success(Course[i].GetHeight(), Course[i].GetRisk())
    total = total1 + chance
    print("The horse ", Horses[0].GetName(), " at fence ", i + 1, " has a ", round(chance, 2), "% chance of success")
average1 = total1 / 4
for i in range(4):
    chance = Horses[1].Success(Course[i].GetHeight(), Course[i].GetRisk())
    total2 = total2 + chance
    print("The horse ", Horses[1].GetName(), " at fence ", i + 1, " has a ", round(chance, 2), "% chance of success")
average2 = total2 / 4

heighest = 0
winner = 0
if (average1 > average2):
    winner = 0
    heighest = average1
else:
    winner = 1
    heighest = average2
print("The higest average is ", Horses[winner].GetName(), " with an average success of ", heighest)
