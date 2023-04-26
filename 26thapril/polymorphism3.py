def addNumbers(a,b):
    print(a+b)
def addNumbers2(*args):
    sum=0
    for value in args:
        sum+=value
    print(sum)
def addNumbers3(arg1,arg2,*arg3):
    print(arg1,arg2,arg3)
#def addNumbers(a,b,c=2):
 #   print(a+b+c)
#addNumbers3(10)
addNumbers3(10,20,30)
addNumbers3(10,20,30,40,50,60,70)