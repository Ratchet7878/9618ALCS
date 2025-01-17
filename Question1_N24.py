class EventItem:
    def __init__(self, EventNamep, Typp, Difficultyp):
        self.__EventName = EventNamep
        self.__Type = Typp
        self.__Difficulty = Difficultyp
    
    def GetName(self):
        return self.__EventName
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetEventType(self):
        return self.__Type
    

Group = []
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))

class Character:
    def __init__(self, CharacterNamep, Jumpp, Swimp, Runp, Drivep):
        self.__CharacterName = CharacterNamep
        self.__Jump = Jumpp
        self.__Swim = Swimp
        self.__Run = Runp
        self.__Drive = Drivep
    
    def GetName(self):
        return self.__CharacterName
    
    def CalculateScore(self, eventType, eventDifficulty):
        #setting for which event
        if eventType.lower() == 'jump':
            winChance = self.__Jump
        elif eventType.lower() == 'swim':
            winChance = self.__Swim
        elif eventType.lower() == 'run':
            winChance = self.__Run
        else:
            winChance = self.__Drive
        #calculation of success
        if winChance < eventDifficulty:
            difference = eventDifficulty - winChance
            if difference == 1:
                return 80
            elif difference == 2:
                return 60
            elif difference == 3:
                return 40
            elif difference == 4:
                return 20
        else:
            return 100

Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)

score_Tarz = 0
scorre_Geni = 0

for x in range(5):
    percentage_Tarz = Tarz.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
    percentage_Geni = Geni.CalculateScore(Group[x].GetEventType(), Group[x].GetDifficulty())
    if percentage_Geni == percentage_Tarz:
        print("It was a draw")
    elif percentage_Tarz > percentage_Geni:
        score_Tarz += 1
        print("Tarz won this event")
    else:
        scorre_Geni += 1
        print("Geni has won the event")

if score_Tarz > scorre_Geni:
    print("Tarz has won this group")
else:
    print("Geni has won this group")



