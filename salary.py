class Salary:
    def __init__(self):
        self.basic = int(input("Enter the basic pay: "))     

    def display(self):
        da = self.basic * 0.3
        hra = self.basic * 0.1
        gross = self.basic + da + hra

        # display salary
        print(f"da= {da}")
        print(f"hra= {hra}")
        print(f"gross= {gross}")

obj = Salary()
obj.display()

    
