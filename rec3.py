def dojob(n):
    if n<=2:
        return
    print(n)
    dojob(n-1)
    print(n)
dojob(10)
