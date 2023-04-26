def addNumbers(a,b):
    print(a+b)
def addNumbers2(*args):
    sum=0
    for value in args:
        sum+=value
    print(sum)
#def addNumbers(a,b,c=2):
 #   print(a+b+c)
addNumbers2(10)
addNumbers2(10,20)
addNumbers2(10,20,30)
addNumbers2(10,20,30,40,50,60)