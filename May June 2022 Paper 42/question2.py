import random

ArrayData = [[0] * 10 for a in range(10)]
for i in range(10):
    for j in range(10):
        ArrayData[i][j] = random.randint(1,100)
        ArrayData[i][j] = random.randint(1, 100)
def OutputArray():
    global ArrayData

    for x in range(10):
        for y in range(10):
            print(ArrayData[x][y], " ", end='') #usually print function ends in new line end='' removes
        print("")
print("Before:")
OutputArray()

ArrayLength = 10
for x in range(0, ArrayLength):
    for y in range(0, ArrayLength - 1):
        for z in range(0, ArrayLength - y - 1):
            if (ArrayData[x][z]) > (ArrayData[x][z + 1]):
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z + 1]
                ArrayData[x][z + 1] = TempValue


print("After:")
OutputArray()

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Upper >= Lower:
        return -1
    else:
        Mid = (Lower + (Upper - 1)) // 2 #// is used as DIV
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)


firstcheck = int(input("Enter the fist num: "))
secondcheck = int(input("Enter the second num: "))
x = BinarySearch(ArrayData, 0, 9, firstcheck)
y = BinarySearch(ArrayData, 0, 9, firstcheck)
print(x)
print(y)



