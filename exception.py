try:
    x=1/0
except EOFError:
    print("eof error")
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("zero division error occured")
    #zero division error occured