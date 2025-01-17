class Queue:
    def __init__(self, Headpointerp, Tailpointerp):
        self.QueueArray = [-1 for x in range(100)]
        self.Headpointer = Headpointerp
        self.Tailpointer = Tailpointerp
    
TheQueue = Queue(-1, 0)

def Enqueue(TheData):
    #AQueue is BYREF
    global TheQueue

    if TheQueue.Headpointer == -1:
        TheQueue.QueueArray[TheQueue.Tailpointer] = TheData
        TheQueue.Headpointer = 0
        TheQueue.Tailpointer += 1
        return 1
    elif TheQueue.Tailpointer > 99:
        return -1
    else:
        TheQueue.QueueArray[TheQueue.Tailpointer] = TheData
        TheQueue.Tailpointer += 1
        return 1

def Dequeue():
    global TheQueue
    if TheQueue.Headpointer == -1:
        return -1
    elif TheQueue.Headpointer == TheQueue.Tailpointer:
        return -1
    else:
        theData = TheQueue.QueueArray[TheQueue.Headpointer]
        TheQueue.Headpointer += 1
        return theData


def ReturnAllData():
    global TheQueue

    returnString = ""
    for x in range(TheQueue.Headpointer, TheQueue.Tailpointer):
        returnString = returnString + str(TheQueue.QueueArray[x]) + " "
    return returnString

for x in range(10):
    dataToAdd = int(input("Enter a number greater than 0: "))
    while dataToAdd < 0:
        dataToAdd = int(input("Enter a number greater than 0: "))
    success = Enqueue(dataToAdd)
    if success == -1:
        print("The queue is full")
    else:
        print("Enqueue was successful")

print(ReturnAllData())
result = Dequeue()
if result == -1:
    print("Queue empty")
else:
    print(result)
    
result = Dequeue()
if result == -1:
    print("Queue empty")
else:
    print(result)

print(ReturnAllData())
