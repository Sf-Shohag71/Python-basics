palindrome = input("Enter a list(e.g. [1, 2, 5]): ")
list1 = []
print(list1)
list2 = list1.copy().reverse()

if(list2 == list1):
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")