Jobs = [[0] * 2 for x in range(10)]
#DECLARE NumberOfJobs = 0
NumberOfJobs = 0

def Initialise():

    global Jobs
    global NumberOfJobs

    for x in range(10):
        Jobs[x][0] = -1
        Jobs[x][1] = -1
    
    NumberOfJobs = 0

def AddJob(JobNum, JobPriority):

    global Jobs
    global NumberOfJobs
    
    added = False
    x = 0
    while not added and x != 9:
        if Jobs[x][0] == -1:
            Jobs[x][0] = JobNum
            Jobs[x][1] = JobPriority
            NumberOfJobs += 1
            added = True
        else:
            x += 1
    if added:
        print("Added")
    else:
        print("Not added")

Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

print(Jobs)
def InsertionSort():

    global Jobs
    global NumberOfJobs

    for x in range(0, NumberOfJobs):

        TempNumber = Jobs[x][0]
        TempPriority = Jobs[x][1]
        TempPointer = x

        while TempPointer > 0 and (Jobs[TempPointer - 1][1] > TempPriority):
            Jobs[TempPointer][0] = Jobs[TempPointer - 1][0]
            Jobs[TempPointer][1] = Jobs[TempPointer - 1][1]
            TempPointer = TempPointer - 1
        Jobs[TempPointer][0] = TempNumber
        Jobs[TempPointer][1] = TempPriority

def PrintArray():

    global Jobs
    global NumberOfJobs

    for x in range(0, NumberOfJobs):
        if Jobs[x][0] != -1:
            print(str(Jobs[x][0]), " priority ", str(Jobs[x][1]))

  

InsertionSort()
PrintArray()







