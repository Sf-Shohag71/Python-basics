import random
class Hat:

    houses = ["Dhaka", "Kazipara", "Laksam", "Kemtoli"]
    
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(f"{name} is in {house}")


Hat.sort("Harry")