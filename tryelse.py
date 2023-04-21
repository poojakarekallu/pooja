try:
    x=1/10
    print("inside try")
except EOFError:
    print("eof error")
except ValueError:
    print("value error occured")
except RuntimeError:
    print("zero division error occured")
else:
    print("control is inside else")
    #inside try
#control is inside else