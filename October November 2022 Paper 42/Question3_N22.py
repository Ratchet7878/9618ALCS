Queue = [0 for x in range(100)]
HeadPointer = 0
TailPointer = 0

def Enqueue(DataToAdd):

    global Queue
    global HeadPointer
    global TailPointer
    
    if TailPointer > 99:
        return False
    else:
        Queue[TailPointer] = DataToAdd
        TailPointer += 1
        return True

flag = True
for x in range(1, 21):

    result = Enqueue(x)
    if not result:
        flag = False

if flag:
    print("Successful")
else:
    print("Uncessful")

def RecursiveOutput(Start):

    #base case
    if Start == 0:
        return Queue[Start]
    else:
        return (Queue[Start] + RecursiveOutput(Start - 1)) #queue start adds the first value and then the function recurses
    
returnvalue = RecursiveOutput(TailPointer - 1)
print(returnvalue)

    