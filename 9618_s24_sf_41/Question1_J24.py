# DECLARE ARRAY:DataStored [1:20] OF INTEGER
DataStored = []
NumberItems = 0

def Initialise():
    global DataStored, NumberItems
    while True:
        userNum = int(input("Enter how many numbers: "))
        if userNum >= 1 and userNum <= 20:
            break
    for x in range(userNum):
        userInput = int(input("Enter the number to store: "))
        DataStored.append(userInput)
        NumberItems += 1

Initialise()
print("Array Contents")
for x in range(NumberItems):
    print(DataStored[x])

def BubbleSort():
    global DataStored, NumberItems
    Pass = NumberItems - 1
    noSwaps = False 
    while not noSwaps:
        noSwaps = True
        for x in range(Pass):
            if DataStored[x] > DataStored[x + 1]:
                DataStored[x], DataStored[x + 1] = DataStored[x + 1], DataStored[x]
                noSwaps = False
        Pass -= 1

BubbleSort()
print("Sorted Array: ", DataStored)

def BinarySearch(DataToFInd):
   
    global DataStored, NumberItems
    Upper = NumberItems
    Lower = 0
    found = False
    isnotpresent = False

    while not found and not isnotpresent:
        Mid = (Lower + Upper) // 2
        if DataStored[Mid] == DataToFind:
            found = True
        elif DataStored[Mid] < DataToFind:
            Lower = Mid + 1
        else:
            Upper = Mid - 1
        if Lower > Upper:
            isnotpresent = True
    print(Mid)
    if isnotpresent:
        return -1 
    else:
        return Mid

dataToFInd = int(input("Enter the data to find: "))
i = BinarySearch(dataToFInd)
if i == -1:
    print("Not found")
else:
    print(dataToFInd, " was found at index ", i)
