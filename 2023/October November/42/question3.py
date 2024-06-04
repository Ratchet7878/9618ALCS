import datetime


class Character:
    def __init__(self, charname, dofb, intel, speedp):
        self.__CharacterName = charname
        self.__DateOfBirth = dofb
        self.__Intelligence = intel
        self.__Speed = speedp

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return  self.__CharacterName

    def SetIntelligence(self, intelligence):
        self.__Intelligence = intelligence

    def Learn(self):
        self.__Intelligence = self.__Intelligence * 1.10

    def ReturnAge(self):
        return 2023 - self.__DateOfBirth.year


FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)
FirstCharacter.Learn()
print("The character's name is " + FirstCharacter.GetName() + ", its age is " + str(FirstCharacter.ReturnAge()) + " and its intelligence is " + str(FirstCharacter.GetIntelligence()))

class MagicClass(Character):
    def __init__(self, elementp, charname, dofb, intel, speedp):
        self.__Element = elementp
        super().__init__(charname, dofb, intel, speedp)

    def Learn(self):
        if self.__Element  == "fire" or self.__Element == "water":
            super().SetIntelligence(super().GetIntelligence() * 1.2)
        elif self.__Element == "earth":
            super().SetIntelligence(super().GetIntelligence * 1.3)
        else:
            super().SetIntelligence(super().GetIntelligence() * 0.9)




FirstMagic = MagicClass("fire", "Light", datetime.datetime(2018, 3, 1), 75, 22)
FirstMagic.Learn()
print("The character's name is " + FirstMagic.GetName() + ", its age is " + str(FirstMagic.ReturnAge()) + " and its intelligence is " + str(FirstMagic.GetIntelligence()))