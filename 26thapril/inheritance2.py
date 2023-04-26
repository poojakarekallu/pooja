class School:
    name="zphs"
    #age=34
    def __init__(self,age):
        self.age=age
    def getAge(self):
        return self.age
class SubSchool(School):
    #def __init__(self):
        #print("child constructor")
    def getParentName(self):
        return "zphs"
    def getName(self):
        return "pooja"
myschool=SubSchool(26)
print(myschool.getParentName())
print(myschool.getName())
print(myschool.getAge())

