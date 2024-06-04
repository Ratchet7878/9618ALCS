ArrayNode = [[-1] * 3 for x in range(20)]
RooPointer = -1
FreeNode = 0


def AddNode():
    global ArrayNode, RooPointer, FreeNode

    DataToEnter = int(input("Enter the data: "))
    if FreeNode <= 19:
        ArrayNode[FreeNode][0] = -1
        ArrayNode[FreeNode][1] = DataToEnter
        ArrayNode[FreeNode][2] = -1
           #check if the root node is free
        if RooPointer == -1:
            RooPointer = 0
        else:
            Placed = False
            currentNode = RooPointer
            while not Placed:
                if DataToEnter < ArrayNode[currentNode][1]:
                #if data is less than, it is placed on left side
                    if ArrayNode[currentNode][0] == -1:
                        ArrayNode[currentNode][0] = FreeNode
                        Placed = True
                    else:
                        currentNode = ArrayNode[currentNode][0]
                else:
                    if ArrayNode[currentNode][2] == -1:
                        ArrayNode[currentNode][2] = FreeNode
                        Placed = True
                    else:
                        currentNode = ArrayNode[currentNode][2]
        FreeNode += 1
    else:
        print("Tree is full!")
        
def PrintAll():
    global ArrayNode, RooPointer, FreeNode

    for x in range(FreeNode):
        print(ArrayNode[x][0], " ", ArrayNode[x][1], " ", ArrayNode[x][2])

for i in range(10):
    AddNode()
PrintAll()
 
def InOrder(Array, Root):
    if Array[Root][0] != -1:
        InOrder(Array, Array[Root][0])
    print(Array[Root][1])
    if Array[Root][2] != -1:
        InOrder(Array, Array[Root][2])  

InOrder(ArrayNode, RooPointer)         