arr = []
with open("Universal Data.txt", "r") as file:
    arr = file.read().splitlines()
for x in range(len(arr)):
    arr[x] = int(arr[x])

arr.sort()

#iterative solution
def IterativeBinarySearch(Array, DataToFind):
    UpperBound = len(Array)
    LowerBound = 0
    found = False
    isnotpresent = False


    while not found and not isnotpresent:

        MidPoint = (LowerBound + UpperBound) // 2
        if Array[MidPoint] == DataToFind:
            found = True
        elif Array[MidPoint] < DataToFind:
            LowerBound = MidPoint + 1
        else:
            UpperBound = MidPoint - 1
        if LowerBound > UpperBound:
            isnotpresent = True

    return found

#recursive solution
def BinarySearch(IntegerArray, LowerBound, UpperBound, ToFind):
    if LowerBound > UpperBound:
        return -1
    mid = (LowerBound + UpperBound) // 2
    if IntegerArray[mid] == ToFind:
        return mid
    elif IntegerArray[mid] > ToFind:
        return BinarySearch(IntegerArray, LowerBound, mid - 1, ToFind)
    else:
        return BinarySearch(IntegerArray, mid + 1, UpperBound, ToFind)
