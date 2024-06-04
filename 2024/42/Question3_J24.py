NumberArray = [100, 85, 644, 22, 15, 8, 1]

def RecursiveInsertion(IntegerArray, NumberOfElements):
    if NumberOfElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberOfElements - 1)
        LastItem = IntegerArray[NumberOfElements - 1]
        CheckItem = NumberOfElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = True
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

print("recursive")
print(RecursiveInsertion(NumberArray, 7))

def IterativeInsertion(IntergerArray):
    NumberOfElements = len(IntergerArray)
    for x in range(1, NumberOfElements):
        LastItem = NumberArray[x]
        TempPointer = x
        while TempPointer > 0 and IntergerArray[TempPointer - 1] > LastItem:
            IntergerArray[TempPointer] = IntergerArray[TempPointer - 1]
            TempPointer -= 1
        IntergerArray[TempPointer] = LastItem
        return IntergerArray

print("iterative")
print(IterativeInsertion(NumberArray))

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    else:
        Mid = (First + Last) // 2
        if IntegerArray[Mid] == ToFind:
            return Mid
        elif IntegerArray[Mid] > ToFind:
            return BinarySearch(IntegerArray, First, Mid - 1, ToFind)
        else:
            return BinarySearch(IntegerArray, Mid + 1, Last, ToFind)

sorted_Array = IterativeInsertion(NumberArray)
found = BinarySearch(sorted_Array, 0, 6, 644)
if found == -1:
    print("Not found")
else:
    print("The index it was found is: ", found)