arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(dataToFind):
    global arrayData
    found = False
    for x in range(10):
        if arrayData[x] == dataToFind:
            found = True
    if not found:
        return False
    else:
        return True

datatofind = int(input("Enter the data to find: "))
result = linearSearch(datatofind)
if not result:
    print("the value was not found!")
else:
    print("the value was found")

def bubbleSort():
    global arrayData

    for x in range(10):
        for y in range(9):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp
