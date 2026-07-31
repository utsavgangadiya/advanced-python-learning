# class and object 

class products :
    unit = 100
    price = 299
    types = 10

info = products()
print(products.unit)
print(products.types)

# constructor

class student :
    def __init__(self,fullname):
        self.name = fullname
        print("add new student data...")

s1 = student("utsav gangadiya")
print(s1.name)

fd=12
print(fd)