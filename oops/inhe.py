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

