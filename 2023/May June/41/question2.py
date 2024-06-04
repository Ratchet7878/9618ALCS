class Vehicle:
    def __init__(self, IDp, MaxSpeedp, IncreaseAmountp):
        self.__ID = IDp
        self.__MaxSpeed = MaxSpeedp
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = IncreaseAmountp
        self.__HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def SetCurrentSpeed(self, SetCP):
        self.__CurrentSpeed = SetCP
    def SetHorizontalPosition(self, SetHP):
        self.__HorizontalPosition = SetHP

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
        if (self.__CurrentSpeed > self.__MaxSpeed):
            self.__MaxSpeed = self.__CurrentSpeed
        self.__HorizontalPosition = self.__CurrentSpeed + self.__HorizontalPosition

    def OutputCurrent(self):
        print("The current speed is: " + str(self.__CurrentSpeed))
        print("The horizontal position is: " + str(self.__HorizontalPosition))

class Helicopter(Vehicle):

    def __init__(self, IDp, MaxSpeedp, IncreaseAmountp, VerticalCh, MaxH):
        super().__init__(IDp, MaxSpeedp, IncreaseAmountp)
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalCh
        self.__MaxHeight = MaxH

    def IncreaseSpeed(self):
        self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
        if (self.__VerticalPosition > self.__MaxHeight):
            self.__VerticalPosition = self.__MaxHeight
        # Helicopter has no current speed of its own, needs to inherit:
        Vehicle.SetCurrentSpeed(self, Vehicle.GetCurrentSpeed(self) + Vehicle.GetIncreaseAmount(self))
        if (Vehicle.GetCurrentSpeed(self) > Vehicle.GetMaxSpeed(self)):
            Vehicle.SetCurrentSpeed(self, Vehicle.GetMaxSpeed(self))
        Vehicle.SetHorizontalPosition(self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self))


    def OutputCurrent(self):
        print("The current speed is: " + str(Vehicle.GetCurrentSpeed(self)))
        print("The horizontal position is: " + str(Vehicle.GetHorizontalPosition(self)))
        print("The vertical position is: " + str(self.__VerticalPosition))


Car = Vehicle("Tiger", 100, 20)
helicopter= Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputCurrent()
helicopter.IncreaseSpeed()
helicopter.IncreaseSpeed()
helicopter.OutputCurrent()


