arr=[1,2,3,4,5]
try:
    if len(arr)>=4:
        raise ValueError("array length is greater or equal to 4")
    else:
        print("everything is fine")
except ValueError as err:
    print(err)