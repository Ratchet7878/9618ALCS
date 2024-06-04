class node:
    def __init__(self, datap, nextNodep):
        self.data = datap
        self.nextNode = nextNodep
    

linkedlist = [node(1,1), node(5,4), node(6,7), node(7, -1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0, -1)]

startPointer = 0
emptyList = 5

def outputNodes(startpointer, emptyList):
    global linkedlist

    currentpointer = startPointer
    while currentpointer != -1:
        print(linkedlist[currentpointer].data)
        currentpointer = linkedlist[currentpointer].nextNode

outputNodes(startPointer, emptyList)

def addNode(linkedlist, currentPointer):
    global emptyList
    datatoadd = int(input("Enter the data to add: "))
    #determine if list is full
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newList = node(datatoadd, -1)
        freeList = linkedlist[emptyList].nextNode
        linkedlist[emptyList] = newList
        previouspointer = 0
        while  currentPointer != -1:
            previouspointer = currentPointer
            currentPointer = linkedlist[currentPointer].nextNode
        linkedlist[previouspointer].nextNode = emptyList
        emptyList = freeList
        return True


print(addNode(linkedlist, startPointer))
print(addNode(linkedlist, startPointer))
print("After calling add node")
print("After calling add node")
outputNodes(startPointer,emptyList)




