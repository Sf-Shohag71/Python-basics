class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting. And it is {self.age} years old.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Jhony', 10)
my_dog.sit()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog age is {my_dog.age}.")