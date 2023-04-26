class Parent1:
    def getName(self):
        return "parent1"
class Parent2:
    def getName(self):
        return "parent2"
class Parent3:
    def getName(self):
        return "parent3"
        
class Child(Parent1,Parent2,Parent3):
    def  __init__(self):
        self.getAllParent()
    def getAllParent(self):
        #write custom logic to get all parent classes
        print("child method")
        parent_list=[]
        for base in Child.__bases__:
            parent_list.append(base)
        print(parent_list)
mychild=Child()
#parent_list=[]
#print(mychild.__bases__)
#for base in Child.__bases__:
    #print(base,end=" ")
#print(mychild.__bases__)
#print(mychild.getName())


