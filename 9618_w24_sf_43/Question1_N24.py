def ReadData():
    arr = []
    with open("Data.txt", "r") as file:
        lines = file.read().splitlines()
        arr.extend(lines)
    file.close()
    return arr

def FormatArray(arr):
    concstr = ''
    n = len(arr)
    for i in range(n):
        
        concstr = concstr + arr[i] + " "
    
    return concstr

DataArray = ReadData()
print(FormatArray(DataArray))

def CompareStrings(string1, string2):
    if len(string1) > len(string2):
        n = len(string2)
    else:
        n = len(string1)
    i = 0
    while (i < n):
        if string1[i] > string2[i]:
            return 1
        elif string2[i] > string1[i]:
            return 2
        i += 1

def Bubble(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n - 1):
            val = CompareStrings(arr[j], arr[j + 1])
            if val == 1:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

SortedArray = Bubble(DataArray)
print(FormatArray(SortedArray))