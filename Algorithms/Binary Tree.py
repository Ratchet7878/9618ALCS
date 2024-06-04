class Node():
    #PUBLIC LeftPointer: INTEGER
    #PUBLIC Data: INTEGER
    #PUBLIC RightPointer: INTEGER
    def __init__(self, LeftPointerP, DataP, RightPointerP):
        self.LeftPointer = LeftPointerP
        self.Data = DataP
        self.RightPointer = RightPointerP


#DECLARE ArrayNodes: ARRAY[1:20, 1:3] OF Node
#DECLARE RootPointer: INTEGER
#DECLARE FreeNode: INTEGER
ArrayNodes = []
for x in range(20):
    ArrayNodes.append(Node(-1, -1, -1))

RootPointer = -1
FreeNode = 0



def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode

    Item = int(input("Please enter the data you want to store: "))
    #checks if the tree is full
    if FreeNode <= 19:

        ArrayNodes[FreeNode] = Node(-1, Item, -1)


        if RootPointer == -1:
            RootPointer = 0
        else:
            CurrentPointer = RootPointer
            Placed = False
            while Placed == False:
                if Item < ArrayNodes[CurrentPointer].Data:
                    if ArrayNodes[CurrentPointer].LeftPointer == -1:
                        ArrayNodes[CurrentPointer].LeftPointer = FreeNode
                        Placed = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer].LeftPointer

                else:
                    if ArrayNodes[CurrentPointer].RightPointer == -1:
                        ArrayNodes[CurrentPointer].RightPointer = FreeNode
                        Placed = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer].RightPointer
        FreeNode = FreeNode + 1
    else:
        print("The tree is Full")

def FindNode(SearchItem):
    global ArrayNodes

    currentPointer = RootPointer
    while currentPointer != -1 and ArrayNodes[currentPointer].Data != SearchItem:
        if SearchItem < ArrayNodes[currentPointer].Data:
            currentPointer = ArrayNodes[currentPointer].LeftPointer
        else:
            currentPointer = ArrayNodes[currentPointer].RightPointer
    return currentPointer

def PrintAll():
    for X in range(0, 20):
        print(ArrayNodes[X].LeftPointer, ArrayNodes[X].Data, ArrayNodes[X].RightPointer)

#Treversal functions
#InOrder = Visits left node, then root and then right node
def InOrder(Array, Root):
    if Array[Root][0] != -1:
        InOrder(Array, Array[Root][0])
    print(str(Array[Root][1]))
    if Array[Root][2] != -1:
        InOrder(Array, Array[Root][2])
#PostOrder = visits left node, then right node and then root
def PostOrder(Array, Root):
    if Array[Root][0] != -1:
        PostOrder(Array, Array[Root][0])
    if Array[Root][2] != -1:
        PostOrder(Array, Array[Root][2])
    print(Array[Root][1])
#PreOrder = visits root node, then left node and then right node
def PreOrder(Array, Root):
    print(str(Array[Root][1]))
    if Array[Root][0] != -1:
        PreOrder(Array, Array[Root][0])
    if Array[Root][2] != -1:
        PreOrder(Array, Array[Root][2])