class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name!")
        self.name = name

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

wizard = Wizard("Gusto")
professor = Professor("SF", "Defense of the black magic")
Student = Student("Harry", "Griffidore")