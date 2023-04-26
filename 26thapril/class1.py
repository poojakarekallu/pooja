class Book:
    numberOfPages=145
    author="pooja"
    scope="To be sold in india"
    def __init__(self,zone,dob):
        self.zone=zone
        self.dob=dob
mybook=Book("Mystery","25-04-23")
print(mybook.numberOfPages)
print(mybook.zone)
print(mybook.dob)