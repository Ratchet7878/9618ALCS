class SaleData:
    def __init__(self, IDP, QuantityP):
        self.ID = IDP
        self.Quantity = QuantityP

CircularQueue = [] #Record array
Head = 0
Tail = 0
NumberOfItems = 0
for x in range(5):
    CircularQueue.append(SaleData("", -1))

def Enqueue(InValue):
    global Head
    global Tail
    global NumberOfItems
    global CircularQueue

    if NumberOfItems == 5:
        return -1
    else:
        CircularQueue[Tail] = InValue
        NumberOfItems += 1
        if Tail == 4: #since this is circular queue
            Tail = 0
        else:
            Tail += 1

        return 1

def Dequeue():
    global Head
    global Tail
    global NumberOfItems
    global CircularQueue

    returnRecord = SaleData("", -1)
    if NumberOfItems == 0:
        return returnRecord
    else:
        returnRecord = CircularQueue[Head]
        NumberOfItems = NumberOfItems - 1
        if Head == 4:
            Head = 0
        else:
            Head += 1
        return returnRecord

def EnterRecord():
    global Head
    global Tail
    global NumberOfItems
    global CircularQueue

    ID = input("Enter an ID: ")
    Quantity = input("Enter a quantity: ")
    InputRecord = SaleData(ID, Quantity)

    result = Enqueue(InputRecord)
    if result == -1:
        print("Full")
    else:
        print("Stored")

EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
EnterRecord()
x = Dequeue()
if x.ID == "":
    print("Error. The queue is empty.")
else:
    print(x.ID + " " + x.Quantity)
EnterRecord()
for x in range(6):
    print(CircularQueue[x].ID + " " + CircularQueue[x].Quantity)



