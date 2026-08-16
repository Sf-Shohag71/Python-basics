print("Enter two number and I will add the numbers (enter 'q' to quit the program).")

while True:
    try:
        # Take user input and try to convert it into a int value
        first_number = input("Enter first number: ")
        if first_number == 'q':
            break
        first_number = int(first_number)
        
        second_number = input("Enter second number: ")
        if second_number == 'q':
            break
        second_number = int(second_number)
        
        # Add two numbers
        addition = first_number + second_number
    except ValueError:
        print("Sorry I really needed a number!")
    else:
        print(f"The summation of {first_number} and {second_number} is: {addition}")