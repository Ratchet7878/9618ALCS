# DECLARE ARRAY:DataStored [1:20] OF INTEGER
DataStored = [0 for x in range(20)]
NumberItems = 0

def Initialise():
    global DataStored, NumberItems
    while True:
        userNum = int(input("Enter how many numbers: "))
        if userNum >= 1 and userNum <= 20:
            break
    for x in range(userNum):
        userInput = int(input("Enter the number to store: "))
        DataStored[x] = userInput
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
