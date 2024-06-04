#9618/41/M/J/21

#Declare node using record data type
class node:
    def __init__(self, DataP, nextNodeP):
        self.Data = DataP #stores the data value of the node
        self.nextNode = nextNodeP #stores the address of next node

linkedlist = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0, 6), node(0,8), node(56, 3), node(0, -1)]

startPointer = 0
emptyList = 5

def OutputNodes(linkedlist, currentPointer):
    while currentPointer != -1:
        print((str(linkedlist[currentPointer].Data))) #prints the data value for the node in the class
        currentPointer = linkedlist[currentPointer].nextNode #goes to the current node and gets the value of the nextnode from that node

def addNode(linkedlist, currentPointer, emptyList):
    dataToAdd = int(input("Enter data to add: "))

    #check if list is full
    if emptyList < 0 or emptyList > 9:
        return False
    else:
        newNode = node(dataToAdd, -1) #creates a new node that is pointing to null
        freeList = linkedlist[emptyList].nextNode
        linkedlist[emptyList] = newNode #inserts the node to the first empty node

        #finding the last node to insert the new node//updating empty list
        previousPointer = 0
        while currentPointer != -1:
            previousPointer = currentPointer
            currentPointer = linkedlist[currentPointer].nextNode
        linkedlist[previousPointer].nextNode = emptyList
        emptyList = freeList

        return True

def deleteNode(datatodelete):

    global linkedlist, startPointer, emptyList

    currentPointer = startPointer

    previousPointer = 0
    #finding the data node to delete
    while currentPointer != -1 and linkedlist[currentPointer].Data != datatodelete:
        previousPointer = currentPointer
        currentPointer = linkedlist[currentPointer].nextNode

    #check if list is empty or full
    if currentPointer == -1:
        return False
    else:
        #update pointers to remove node
        if currentPointer == startPointer:
            startPointer = linkedlist[startPointer].nextNode #if data to delete is in first node
        else:
            linkedlist[previousPointer].nextNode = linkedlist[currentPointer].nextNode

        linkedlist[currentPointer].data = 0
        linkedlist[currentPointer].nextNode = emptyList
        emptyList = currentPointer

        return True


def FindItem(currentPointer, Searchvalue):
    while currentPointer != -1:
        if linkedlist[currentPointer].Data != Searchvalue:
            currentPointer = linkedlist[currentPointer].nextNode
        else:
            return currentPointer

    currentPointer = -1
    return currentPointer

#inserting in ordered linked list

def OrderedInsertion(currentPointer, linkedlist, emptylist, startpointer, datatoinsert):
    if emptylist < 0 or emptylist > 9:
        return False
    else:
        freelist = emptylist
        emptylist = linkedlist[emptylist].nextNode

        newNode = node(datatoinsert, -1)
        linkedlist[freelist] = newNode

        while currentPointer != -1 and linkedlist[currentPointer].Data < datatoinsert:
            previouspointer = currentPointer
            currentPointer = linkedlist[currentPointer].nextNode

        if currentPointer == startPointer:
            linkedlist[freelist].nextNode = startpointer
            startpointer = freelist
        else:
            linkedlist[freelist].nextNode = linkedlist[previouspointer].nextNode
            linkedlist[previouspointer].nextNode = freelist

        return True