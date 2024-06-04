arr = []
with open("Universal Data.txt", "r") as file:
    arr = file.read().splitlines()
for x in range(len(arr)):
    arr[x] = int(arr[x])

NumberArray = [100, 85, 644, 22, 15, 8, 1]
#Iterative Insertion Sort
def iterative_insertion_sort(Array):
    length_Array = len(Array)
    for x in range(1, length_Array):
        TempValue = Array[x]
        TempPointer = x
        #sorts in ascending order
        while TempPointer > 0 and Array[TempPointer] > TempValue:
            Array[TempPointer] = Array[TempPointer - 1]
            TempPointer -= 1
        Array[TempPointer] = TempValue
        return Array 


#Recursive Insertion Sort (pseudocode will usually be given)
def recursive_insertion_sort(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        recursive_insertion_sort(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2

        while CheckItem >= 0 and IntegerArray[CheckItem] > LastItem:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem -= 1

        IntegerArray[CheckItem + 1] = LastItem
        return IntegerArray


