QueueArray = ['' for x in range(10)]
HeadPointer = 0
TailPointer = 0
NumberOfItems = 0

def Enqueue(DataToAdd):
    #for byref we need to pass as global

    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems

    if NumberOfItems == 10:
        return False
    else:
        QueueArray[TailPointer] = DataToAdd
        #since queue is circular tail pointer goes back in length is exceeded
        if TailPointer >= 9:
            TailPointer = 0
        else:
            TailPointer += 1
        NumberOfItems += 1
        return True

def Dequeue():

    global QueueArray
    global HeadPointer
    global TailPointer
    global NumberOfItems

    if NumberOfItems == 0:
        return False
    else:
        outputval = QueueArray[HeadPointer]
        HeadPointer += 1
        #since queue is circular head pointer goes back in length is exceeded
        if HeadPointer >= 9 or HeadPointer == TailPointer:
            HeadPointer = 0
        NumberOfItems = NumberOfItems - 1

        return outputval


for y in range(11):
    invalue = input("Enter a string value: ")
    enqueueresult = Enqueue(invalue)
    if not enqueueresult:
        print("The enqueue was not successful!")
    else:
        print("Enqueue was successful")

for z in range(2):
    dequeueval = Dequeue()
    if dequeueval:
        print(dequeueval)





