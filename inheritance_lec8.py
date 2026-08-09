class Car:
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("SUV")
# car1.start()


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    
    # def calPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
    
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"
        
stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 87
print(stu1.phy)
print(stu1.percentage)
