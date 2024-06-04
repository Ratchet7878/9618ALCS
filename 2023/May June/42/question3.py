class Employee:
    def __init__(self, HourlyPayp, EmployeeNumberp, JobTitlep):
        self.__HourlyPay = HourlyPayp
        self.__EmployeeNumber = EmployeeNumberp
        self.__JobTitle = JobTitlep
        self.__PayYear2022 = [] # array of 52 elements
        for x in range(52):
            self.__PayYear2022.append(0.0)

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, Week, Hours):
        self.__PayYear2022[Week - 1] = float(Hours) * float(self.__HourlyPay)

    def GetTotalPay(self):
        onektaka = 0
        for x in range(52):
            onektaka = onektaka + self.__PayYear2022[x]
        return onektaka

class Manager(Employee):
    def __init__(self, HourlyPayp, EmployeeNumberp, JobTitlep, Bonus):
        super().__init__(HourlyPayp, EmployeeNumberp, JobTitlep)
        self.__BonusValue = Bonus

    def SetPay(self, Week, Hours):
        Hours = float(Hours) * (1+ (self.__BonusValue /100))
        super().SetPay(Week, Hours)  # Call the method for the instance of the class


EmployeeArray = [] # global array of 8
filename = "Employees.txt"
Bonus = 0
try:
    filedata = open(filename, 'r')
    for i in range(8):
        pay = filedata.readline().strip()
        ID = filedata.readline().strip()
        Temp = filedata.readline().strip()
        try:
            Bonus = float(Temp)
            Title = filedata.readline().strip()
            EmployeeArray.append(Manager(pay, ID, Title, Bonus))
        except:
            EmployeeArray.append(Employee(pay, ID, Temp))
except IOError:
    print("File Not Found")

def EnterHours():
    filename = "HoursWeek1.txt"
    try:
        filedata = open(filename, 'r')
        for i in range(8):
            employnum = filedata.readline().strip()
            hourpay = filedata.readline().strip()
            for j in range(8):
                if EmployeeArray[j].GetEmployeeNumber() == employnum:
                    EmployeeArray[j].SetPay(1, hourpay)
    except IOError:
        print("File not found!")

EnterHours()
for a in range(8):
    print(EmployeeArray[a - 1].GetEmployeeNumber() + " " + str(EmployeeArray[a - 1].GetTotalPay()))







