class Pictures:
    def __init__(self, Descriptionp, Widthp, Heightp, Framecolorp):
        self.__Description = Descriptionp
        self.__Width = Widthp
        self.__Height = Heightp
        self.__FrameColour = Framecolorp
    
    def GetDescription(self):
        return self.__Description
    
    def GetHeight(self):
        return self.__Height
    
    def GetWidth(self):
        return self.__Width
    
    def GetColour(self):
        return self.__FrameColour
    
    def SetDescription(self, newdescription):
        self.__Description = newdescription
    

Picture = [] #array of 100 elements
def ReadData():
    global Picture
    count = 0
    try:
        file = open("Pictures.txt", "r")
        description = file.readline().strip()
        while description != "":
            width = int(file.readline().strip())
            height = int(file.readline().strip())
            framecolor = file.readline().strip()
            Picture.append(Pictures(description, width, height, framecolor))
            count += 1
            description = file.readline().strip()
        return count
    except FileNotFoundError:
        print("The file was not found!")
        return count

noofpictures = ReadData()
framecolour = input("Enter the frame color: ")
framecolour = framecolour.lower()
maxwidth = int(input("Enter the maximum width: "))
maxheight = int(input("Enter the max height: "))
for x in range(noofpictures):
    if framecolour == (Picture[x].GetColour()).lower() or maxwidth == Picture[x].GetWidth() or maxheight == Picture[x].GetHeight():
        print(Picture[x].GetDescription())
        print(Picture[x].GetWidth())
        print(Picture[x].GetHeight())
    

