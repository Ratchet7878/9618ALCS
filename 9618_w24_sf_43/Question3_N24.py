LinkedList = [[0] * 2 for x in range(20)]
for i in range(20):
    LinkedList[i][0] = -1
    LinkedList[i][1] = i + 1
LinkedList[19][0] = -1
LinkedList[19][1] = -1 #end of the linked list
FirstEmpty = 0 #next pointer
FirstNode = -1 #current pointer

def InsertData():
    global FirstNode, FirstEmpty, LinkedList
    data = int(input("Enter data to enter to linked list : "))
    if FirstEmpty != -1:
        nextEmpty = LinkedList[FirstEmpty][1]
        LinkedList[FirstEmpty][0] = data
        LinkedList[FirstEmpty][1] = FirstNode
        FirstNode = FirstEmpty
        FirstEmpty = nextEmpty

def OutputLinkedList():
    global FirstNode, FirstEmpty, LinkedList

    currentPointer = FirstNode
    end = False
    while not end:
        print(LinkedList[currentPointer][0])
        currentPointer = LinkedList[currentPointer][1]
        if currentPointer == -1:
            end = True
        

def RemoveData(data):
    global FirstEmpty, FirstNode, LinkedList
    #if its the first value
    if LinkedList[FirstNode][0] == data:
        currentFirst = LinkedList[FirstNode][1]
        LinkedList[FirstNode][1] = FirstEmpty #updates starting of the empty list
        FirstEmpty = FirstNode
        FirstNode = currentFirst
    else:
        if FirstNode != -1:
            current = FirstNode
            previous = -1 
            while (data != LinkedList[current][0] and current != -1):
                previous = current
                current = LinkedList[current][1]
            
            if data == LinkedList[current][0]:
                LinkedList[previous][1] = LinkedList[current][1]
                LinkedList[current][0] = -1 
                LinkedList[current][1] = FirstEmpty
                FirstEmpty = current

for i in range(5):
    InsertData()

OutputLinkedList()




