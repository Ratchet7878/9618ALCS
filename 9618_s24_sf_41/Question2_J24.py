class Tree:
    def __init__(self, TreeNamep, HeightGrowthp, MaxHeightp, MaxWidthp, Evergreenp):
        self.__TreeName = TreeNamep
        self.__HeightGrowth = HeightGrowthp
        self.__MaxHeight = MaxHeightp
        self.__MaxWidth = MaxWidthp
        self.__Evergreen = Evergreenp
    
    def GetTreeName(self):
        return self.__TreeName
    
    def GetGrowth(self):
        return self.__HeightGrowth
    
    def GetMaxHeight(self):
        return self.__MaxHeight
    
    def GetMaxWidth(self):
        return self.__MaxWidth
    
    def GetEvergreen(self):
        return self.__Evergreen
    
Tree_Array = []
def ReadData():
        
        try:
            file = open("Trees.txt", "r")
            for x in range(0, 9):
                filedata = file.readline().strip()
                name, heightgrowth, height, width, ever = filedata.split(",")
                Tree_Array.append(Tree(name, int(heightgrowth), int(height), int(width), ever))
            file.close()
            return Tree_Array
        except IOError:
            return "File not found"
        
def PrintTrees(Tree_Obj):
    if Tree_Obj.GetEvergreen() == "No":
        print(Tree_Obj.GetTreeName(), " has a maximum height ", Tree_Obj.GetMaxHeight(), " a maximum width ", Tree_Obj.GetMaxWidth(), " and grows ", Tree_Obj.GetGrowth(), " cm a year. It does not lose its leaves.")
    else:
        print(Tree_Obj.GetTreeName(), " has a maximum height ", Tree_Obj.GetMaxHeight(), " a maximum width ", Tree_Obj.GetMaxWidth(), " and grows ", Tree_Obj.GetGrowth(), " cm a year. It loses its leaves each year.")

ret_array = ReadData()
PrintTrees(ret_array[0])



New_Tree = []
def ChooseTree(Tree_Array):
    u_height = int(input("Enter the maximum height the tree can be in cm: "))
    u_width = int(input("Enter the maximum width the tree can be in cm: "))
    u_ever = input("Enter whether the tree is evergreen, or not evergreen: ")
    for x in range(len(Tree_Array)):
        if Tree_Array[x].GetMaxHeight() <= u_height and Tree_Array[x].GetMaxWidth() <= u_width and Tree_Array[x].GetEvergreen().lower() == u_ever.lower():
            New_Tree.append(Tree_Array[x])
    if len(New_Tree) == 0:
        print("No suitable trees")
    else:
        for x in range(len(New_Tree)):
            PrintTrees(New_Tree[x])
    user_choice = input("Name of the tree to purchase: ")
    starting_height = int(input("Enter starting height: "))
    for x in range(len(New_Tree)):
        if user_choice == New_Tree[x].GetTreeName():
            choice_obj = New_Tree[x]
            break
    years_to_live = (choice_obj.GetMaxHeight() - starting_height) // choice_obj.GetGrowth()
    print("The tree’s height is ", starting_height, " when bought. The tree will take ", years_to_live, " years to reach its maximum height of ", choice_obj.GetMaxHeight())



ChooseTree(ret_array)