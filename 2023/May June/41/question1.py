DataArray = [[0] for x in range(25)]

file = open("Data.txt", "r")
for x in range(25):
    filedata = file.readline().strip()
    DataArray[x] = int(filedata)

def PrintArray(DataArray):
    lenarray = len(DataArray)
    outstring = ""
    for x in range(lenarray):
        data = DataArray[x]
        outstring = outstring + str(data) + " "
    print(outstring)

PrintArray(DataArray)
def LinearSearch(Array, SearchValue):
    count = 0
    for x in range(len(Array)):
        if (Array[x] == SearchValue):
            count += 1
    return count

value = int(input("Enter an integer between 0 and 100: "))
while value < 0 or value > 100:
    print("Incorrect value, enter again.")
    value = int(input("Enter an integer between 0 and 100: "))

result = LinearSearch(DataArray, value)
print("The number " + str(value) + " is found " + str(result) + " times.")


