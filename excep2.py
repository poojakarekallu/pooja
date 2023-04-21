try:
    x=1/0
except EOFError:
    print("eof error")
except ValueError:
    print("value error occured")
except RuntimeError:
    print("zero division error occured")
    #x=1/0
#ZeroDivisionError: division by zero