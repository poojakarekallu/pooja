num=int(input("enter a num: "))
temp=num
sum=0
while num!=0:
    rem=num%10;                                        
    sum=sum+rem*rem*rem;                                       
    num=num//10; 
if temp==sum:
    print("armstrong")
else:
    print("not a armstrong")
