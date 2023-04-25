arr=[1,2,3,1,2,4,5,6]
myset=set(arr)
print(myset)
for ele in myset:   #accessing elements
    print(ele,end=" ")
print()
myset.add(34)
print(myset)
myset.copy()
print(myset)
myset.clear()
print(myset)


