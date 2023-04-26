class Animal:
    def printSomething(self):
        print("Animals are good by nature")
    def canFly(self,name):
        if(name=="pooja"):
            print("animal pooja can fly")
        else:
            print("no animals can fly")
class Dog(Animal):
    def canFly(self):
        print("dogs can not fly")
class Pooja(Animal):
    def canFly(self):
        print("pooja can fly")
mypooja=Pooja()
mypooja.canFly()
#mypooja.canFly("pooja") you cannot access parent class methd bcz the method is already present in child class
#if you want acces parent class method canFly you want to create object for parent class and acess it