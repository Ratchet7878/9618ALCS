Animal = [[""] for x in range(20)]
Colour = [[""] for y in range(10)]

AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData


def PushColor(DataToPush):
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 20:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData

def ReadData():
    try:
        animalfile = "AnimalData.txt"
        colourfile = "ColourData.txt"
        file_animal = open(animalfile, "r")
        file_colour = open(colourfile, "r")
        filedata_animal = file_animal.readline().strip()
        filedata_colour = file_colour.readline().strip()
        while filedata_animal != "":
            PushAnimal(str(filedata_animal))
            filedata_animal = file_animal.readline().strip()
        file_animal.close()
        while filedata_colour != "":
            PushColor(str(filedata_colour))
            filedata_colour = file_colour.readline().strip()
        file_colour.close()
    except FileExistsError:
        print("File does not exist")

def OutputItem():
    color = PopColour()
    animal = PopAnimal()
    if animal == "":
        PushColor(color)
    elif color == "":
        PushAnimal(animal)
    else:
        print(color + " " + animal)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()