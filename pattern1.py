n=int(input("enter a value: "))
i=1
j=1
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()