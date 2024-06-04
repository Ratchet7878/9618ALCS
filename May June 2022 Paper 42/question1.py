StackData = [0 for x in range(10)]
StackPointer = 0

def OutputElements():
    global StackData
    global StackPointer

    for x in range(10):
        print(StackData[x])
    print(StackPointer)

def Push(InValue):

    global StackData
    global StackPointer

    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = InValue
        StackPointer += 1
        return True


def Pop():
    global StackData
    global StackPointer

    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer - 1
        returnvalue = StackData[StackPointer]
        StackData[StackPointer] = 0
        return returnvalue

for i in range(11):
    userinput = int(input("Enter an integer value: "))
    resultflag = Push(userinput)
    if resultflag:
        print("The insertion was successful")
    else:
        print("Stack is full")

val1 = Pop()
val2 = Pop()
print(val1, val2)
print(StackData)