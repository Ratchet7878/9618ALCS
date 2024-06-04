class Node:
    def __init__(self, datap):
        self.__Data = datap
        self.__LeftPointer = -1
        self.__RightPointer = -1
    
    def GetLeft(self):
        return self.__LeftPointer
    
    def GetRight(self):
        return self.__RightPointer
    
    def GetData(self):
        return self.__Data
    
    def SetLeft(self, Leftp):
        self.__LeftPointer = Leftp
    
    def SetRight(self, Rightp):
        self.__RightPointer = Rightp
    
    def SetData(self, Datap):
        self.__Data = Datap

class TreeClass:
    def __init__(self):
        self.__FirstNode = -1
        self.__NumberNode = 0
        self.__Tree = []
        for x in range(20):
            self.__Tree.append(-1)
        
    def InsertNode(self, NewNode):
        if self.__NumberNode <= 19:
            self.__Tree[self.__NumberNode] = NewNode
            if self.__FirstNode == -1:
                self.__FirstNode = 0
            else:
                Placed = False
                currentPointer = self.__FirstNode 
                while not Placed:
                    if NewNode.GetData() < self.__Tree[currentPointer].GetData():
                        if self.__Tree[currentPointer].GetLeft() == -1:
                            self.__Tree[currentPointer].SetLeft(self.__NumberNode)
                            Placed = True
                        else:
                            currentPointer = self.__Tree[currentPointer].GetLeft()
                    else:
                        if self.__Tree[currentPointer].GetRight() == -1:
                            self.__Tree[currentPointer].SetRight(self.__NumberNode)
                            Placed = True
                        else:
                            currentPointer = self.__Tree[currentPointer].GetRight()
            self.__NumberNode += 1
        else:
            print("The tree is full")

    def OutputTree(self):
        for x in range(self.__NumberNode):
            print(self.__Tree[x].GetLeft(), "   ", self.__Tree[x].GetData(), "  ", self.__Tree[x].GetRight())


TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()
