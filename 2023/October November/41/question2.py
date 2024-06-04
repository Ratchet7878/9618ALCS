Queue = ["" for x in range(50)]
HeadPointer = -1
TailPointer = 0

Records = [] #array of type RecordData [1:50]
NumberRecords = 0

def Enqueue(Value):
    global Queue, HeadPointer, TailPointer
    if TailPointer >= 50:
        print("The Queue is full!")
    else:
        Queue[TailPointer] = Value
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Empty")
    else:
        FirstValue = Queue[HeadPointer]
        Queue[HeadPointer] = ""
        HeadPointer += 1
        return FirstValue

def ReadData():
    global Queue, HeadPointer, TailPointer
    try:
        file = open("QueueData.txt", "r")
        filedata = file.readline().strip()
        while filedata != "":
            Enqueue(filedata)
            filedata = file.readline().strip()
        file.close()
    except FileNotFoundError:
        print("File doesn't exist")

class RecordData:
    def __init__(self, IDp, Totalp):
        self.ID = IDp
        self.Total = Totalp


def TotalData():
    global Queue, HeadPointer, TailPointer, Records, NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records.append(RecordData(DataAccessed, 1))
        Flag = True
        NumberRecords += 1
    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total = (Records[x].Total) + 1
                Flag = True

    if not Flag:
        Records.append(RecordData(DataAccessed, 1))
        NumberRecords += 1

def OutputRecords():
    global Records, NumberRecords
    for x in range(0, NumberRecords):
        print("ID ", str(Records[x].ID), " Total ", str(Records[x].Total))

ReadData()
print(Queue)
while HeadPointer != TailPointer:
    TotalData() # until all the records are dequeued

OutputRecords()
