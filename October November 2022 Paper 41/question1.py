DataArray = [0 for x in range(100)]

filename = "IntegerData.txt"


def ReadFile():
    global DataArray
    global filename
    file = open(filename, "r")
    try:
        for x in range(len(DataArray)):
            filedata = file.readline().strip()
            DataArray[x] = int(filedata)
    except IOError:
        print("File not found")


def FindValues():
    global DataArray

    count = 0
    findvalue = int(input("Enter a number: "))
    while findvalue < 1 or findvalue > 100:
        findvalue = input(int("Enter a number: "))
    for x in range(len(DataArray)):
        if DataArray[x] == findvalue:
            count += 1

    return count

ReadFile()
x = FindValues()

print("The value was found " + str(x) + "times.")

def BubbleSort():
    global DataArray

    Pass = len(DataArray) - 1
    noswap = False
    while not noswap:
        noswap = True
        for y in range(0, Pass):
            if DataArray[y] > DataArray[y + 1]:
                temp = DataArray[y]
                DataArray[y] = DataArray[y + 1]
                DataArray[y + 1] = temp
                noswap = False
    Pass = Pass - 1
    print(DataArray)

BubbleSort()