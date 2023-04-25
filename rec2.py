def dojob2(n):
    if n<=5:
        return
    dojob2(n-1)
    print(n)
    dojob2(n-1)
    print(n)
dojob2(8)
