QueueArray = [0 for x in range(20)]
HeadPointer = 0 #points to the first element of the queue
TailPointer = 0 #points to the next available space in the queue
NumberOfItems = 0 #to check if the queue is free in the case of implementing a circular queue

def Enqueue(DataToAdd):
    global QueueArray, HeadPointer, TailPointer, NumberOfItems
    if NumberOfItems == len(QueueArray):
        print("Queue is full")
        return False
    else:
        QueueArray[TailPointer] = DataToAdd
        NumberOfItems += 1
        #only implement if the queue is circular
        if TailPointer >= len(QueueArray):
            TailPointer = 0
        else:
            TailPointer += 1
        return True

def Dequeue():
    global QueueArray, HeadPointer, TailPointer, NumberOfItems
    if NumberOfItems == 0 :
        print("The queue is empty")
        return -1
    else:
        DequeuedVal = QueueArray[HeadPointer]
        #only implement if the queue is circular
        if HeadPointer >= len(QueueArray) or HeadPointer == TailPointer:
            HeadPointer = 0
        else:
            HeadPointer += 1
        return DequeuedVal
