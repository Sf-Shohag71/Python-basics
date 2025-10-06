# creating a class
class Student:
    def __init__(self, name):
        self.name = name
        # print(self)
        # print("This is a constructor")
        
    def welcome(self):
        print("Welcome to the class,", self.name)
        

s1 = Student("shohag")
# print(s1.name)
# s1.welcome()


# Create student class that takes name & marks of 3 subjects as arguments in constructor, then create a method to print average.

class Student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        print("Hello", self.name, "Your average marks is:", sum/len(self.marks))
        
s2 = Student2("SF", [80, 90, 95])
s2.get_avg()