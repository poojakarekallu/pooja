try:
    x=1/0
except ZeroDivisionError as err:
    print(err)
finally:
    print("finally will always gets executed")
    #division by zero
#finally will always gets executed 