class CustomException(Exception):
    "this is custom exception"
    pass
try:
    x=20
    if x==20:
        raise CustomException
    else:
        print("x is not 20")
except CustomException as err:
    print("exception occured")
#exception occured