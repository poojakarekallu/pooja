class Book:
    numberOfPages=145
    author="pooja"
    scope="To be sold in india"
    def __init__(self,zone):
        self.zone=zone
mybook=Book("Mystery")
print(mybook.numberOfPages)
print(mybook.zone)
