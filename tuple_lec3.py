# Write a program to count the number of students with the "A" grade in the following tuple. 
# ["C", "D", "A", "A", "B", "A", "C", "B", "A"]

grades = ("C", "D", "A", "A", "B", "A", "C", "B", "A")
print(grades.count("A"))

# Store the above values in a list and sort them from "A" to "D".
grades_list = list(grades)
print(grades_list)
grades_list.sort()
print(grades_list)