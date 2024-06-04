StackVowel = ["" for x in range(100)]
StackConsonant = ["" for x in range(100)]

VowelTop = 0
ConsonantTop = 0

def PushData(InLetter):

    global VowelTop
    global ConsonantTop
    global StackVowel
    global StackConsonant

    Letterval = InLetter.lower()

    if Letterval == "a" or Letterval == "e" or Letterval == "i" or Letterval == "o" or Letterval == "u":
        if VowelTop == len(StackVowel):
            print("Stack is full")
        else:
            StackVowel[VowelTop] = InLetter
            VowelTop += 1
    else:
        if ConsonantTop == len(StackConsonant):
            print("Stack is full")
        else:
            StackConsonant[ConsonantTop] = InLetter
            ConsonantTop += 1

def ReadData():

    global VowelTop
    global ConsonantTop
    global StackVowel
    global StackConsonant

    try:
        file = open("StackData.txt", "r")
        filedata = file.readline().strip()
        while filedata != "":
            PushData(filedata)
            filedata = file.readline().strip()
    except IOError:
        print("File Not Found")



def PopVowel():

    global VowelTop
    global StackVowel

    if VowelTop == 0:
        return "No data"
    else:
        VowelTop = VowelTop - 1
        returnvalue = StackVowel[VowelTop]
        VowelTop = VowelTop - 1
        return returnvalue

def PopConsonant():

    global ConsonantTop
    global StackConsonant

    if ConsonantTop == 0:
        return "No data"
    else:
        ConsonantTop = ConsonantTop - 1
        returnvalue = StackConsonant[ConsonantTop]
        ConsonantTop = ConsonantTop - 1
        return returnvalue

ReadData()
counter = 1
outputstring = ""
while counter != 6:
    inputdata = input("Enter your choice of a sexy vowel or hot consonant: ")
    if inputdata == "vowel":
        x = PopVowel()
        if x != "No data":
            outputstring = outputstring + x
            counter += 1
        else:
            print("The stack was empty")
    else:
        c = PopConsonant()
        if c != " No Data":
            outputstring = outputstring + c
            counter += 1
        else:
            print("The stack was full")


print(outputstring)

