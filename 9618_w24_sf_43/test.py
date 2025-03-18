LinkedList = [[0] * 2 for x in range(20)]
for i in range(20):
    LinkedList[i][0] = -1
    LinkedList[i][1] = i + 1
LinkedList[19][0] = -1
LinkedList[19][1] = -1 #end of the linked list
FirstEmpty = 0 #next pointer
FirstNode = -1 #current pointer

def InsertData():
    global LinkedList
    global FirstNode
    global FirstEmpty
    for _ in range(5):
        if FirstEmpty != -1:
            nextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][0] = int(input("Value: "))
            LinkedList[FirstEmpty][1] = FirstNode
            FirstNode = FirstEmpty
            FirstEmpty = nextEmpty  

def OutputLinkedList():
    global LinkedList
    global FirstNode
    global FirstEmpty
    CurrentPointer = FirstNode
    Flag = True
    while Flag:
        print(LinkedList[CurrentPointer][0])
        CurrentPointer = LinkedList[CurrentPointer][1]
        if CurrentPointer == -1:
            Flag = False

InsertData()
print(LinkedList)