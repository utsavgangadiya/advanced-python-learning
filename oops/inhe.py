# single inheritance  

class car:
    color="black"
    @staticmethod
    def start():
        print("car stared...")

    @staticmethod
    def stop():
        print("car stoped.")

class toyotocar(car):
    def __init__(self,name):
        self.name = name

car1= toyotocar("fortuner")
car2= toyotocar("prius")

print(car1.name)
print(car1.start())
print(car1.color)

# multi-level inheritance
print("----------------------------")


class car:
    @staticmethod
    def start():
        print("car stared...")

    @staticmethod
    def stop():
        print("car stoped.")

class toyotocar(car):
    def __init__(self,brand):
        self.brand = brand


class fortuner(toyotocar):
    def __init__(self,type):
        self.type = type

car4 = fortuner("diesel")
car4.start()

# multiple inheritance

print("----------------------------")

class A:
    vara="welcome to a"

class B:
    varb="welcome to b"

class C(A,B):
    varc = "welcome to c"

c1 = C()

print(c1.varc)
print(c1.varb)
print(c1.vara)