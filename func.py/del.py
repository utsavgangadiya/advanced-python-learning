class student:
    def __init__(self,name,marks):
        self.name =  name
        self.marks = marks

s1 = student("utsav",[100,98,95])
print(s1.name)

del s1 

print(s1.name)