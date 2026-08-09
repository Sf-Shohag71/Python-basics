def calcSum(a, b):
    sum = a + b
    return sum

result = calcSum(10, 20)
# print("Sum is:", result)

# print("shakh","farid","shohag")
# print("shakhfaridshohag", end=" ")

def calcMul(a=1, b=1):
    mul = a * b
    return mul

multiplication = calcMul(10)
# print("Multiplication is:", multiplication)

cities = ["Dhaka", "Chittagong", "Khulna", "Barishal", "Sylhet", "Rangpur", "Mymensingh", "Rajshahi"]
heros = ["Shakib", "Tamim", "Mushfiq", "Mahmudullah", "Mustafizur", "Mashrafe", "Soumya", "Liton"]

def print_len(list):
    print(len(list))
    
# print_len(cities)
# print_len(heros)

def print_list(list):
    for item in list:
        print(item, end=", ")
        
# print_list(heros)

# factorial calculation
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
    
result = factorial(12)  
# print("Factorial is:", result)


# Convert USD to BDT
def converter(USD):
    BDT = USD * 121.60
    print(USD, "USD =", BDT, "BDT")
result = converter(10)