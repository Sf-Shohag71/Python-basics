# Recursion simple program
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
    print("END")
    
# show(5)

# Factorial of a number using recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

# print(factorial(5))

# print n natural numbers using recursion
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

print(calc_sum(5))

# print list using recursion
def print_list(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)
    
print_list([1,2,3,4,5], 0)