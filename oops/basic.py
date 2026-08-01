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

# ex

class student:
    def __init__(self,name,marks):
        self.name =  name
        self.marks = marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        print("hello",self.name,"your avg score is :",sum/3)

s1 = student("utsav",[100,98,95])
s1.get_avg()
