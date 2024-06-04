StackArray = [0 for x in range(20)]
TopPointer = 0 #points to the next available space in the stack

def Push(DataToEnter):
    global StackArray, TopPointer
    if TopPointer < len(StackArray):
        StackArray[TopPointer] = DataToEnter
        TopPointer += 1
        return True
    else:
        print("Stack is full")
        return False

def Pop():
    global StackArray, TopPointer
    if TopPointer == 0:
        print("Stack is empty")
        return -1
    else:
        TopPointer -= 1
        pushedVal = StackArray[TopPointer]
        StackArray[TopPointer] = 0
        return pushedVal