def fib(n):
    if n<=0:
        print("invalid argument")
        return -1
    if n==1:
        print(0," ",1)
        return -1
    a=0
    b=1
    print(a," ",b)
    count=3
    while count<=n:
        next =a+b
        print(next,end=" ")
        a=b
        b=next
        count=count+1
fib(10)
