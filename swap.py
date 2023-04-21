a=int(input("enter a value: "))
b=int(input("enter b value: "))
c=int(input("enter c value: "))
if a>b and a>c:
    if b>c:
        temp=a
        a=b
        b=c
        c=temp
    else:
        temp=a
        a=b
        b=c
        c=temp
elif b>a and b>c:
    if a<c:
        temp=b
        b=c
        c=temp
    else:
        temp=b
        b=a
        a=c
        c=temp
elif c>a and c>b:
    if a>b:
        temp=b
        b=a
        a=temp
print(a,b,c)
