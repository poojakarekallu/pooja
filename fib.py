n=int(input("enter a num: "))
a=0
b=1
if n<=2:
    print("enter a valid number")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c

    