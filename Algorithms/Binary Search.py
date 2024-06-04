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
