def fib(n):
    if n<0:
        print("invalid")
    elif n==0:
        print("0")
    elif n==1 or n==2:
        print("1")
    else:
        return fib(n-1)+fib(n-2)
fib(5)