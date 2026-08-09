# list1 = [1, 2, 2, 1]
list1 = ["m", "a", "a", "m"]

copy_list1 = list1.copy()
print(copy_list1)
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not a Palindrome")