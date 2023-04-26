class Car:
    engineType="strongest Engine"
    numberOfTyres=4
    numberOfWindows=6
    isFridgeAvailable=True
    def getNumberOfWindows(self):
        return self.numberOfWindows
    def getNumberOfTyres(self):
        return self.numberOfTyres
car1=Car()
print(car1.engineType)
print(car1.getNumberOfWindows())
print(car1.getNumberOfTyres())