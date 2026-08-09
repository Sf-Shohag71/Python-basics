student = {
    "id": 192002038,
    "name": "Shakh Farid Shohag",
    "age": 27,
    "cgpa": 3.48,
    "is_adult": True,
    "subjects": ["CSE", "Math", "English"],
}
student["gender"] = "Male"

# print(student["name"])
# print(student)

# Nested Dictionary
student2 = {
    "id": 192002039,
    "name": "John Doe",
    "age": 25,
    "cgpa": 3.75,
    "is_adult": True,
    "subjects": {
        "physics": 85,
        "math": 90,
        "chemistry": 88
    }
}
# print(student2["subjects"]["math"])
# print(student2["name"])
# print(student2.get("name"))
# print(student2.get("name1"))
# print(list(student2.keys()))

# Write a program to collect subjects and marks of student from user and store them in a dictionary.
subject1 = input("Enter subject 1: ")
marks1 = input("Enter {subject1} marks: ")
subject2 = input("Enter subject 2: ")
marks2 = input("Enter {subject2} marks: ")
subject3 = input("Enter subject 3: ")
marks3 = input("Enter {subject3} marks: ")

marksheet = {}
marksheet[subject1] = marks1
marksheet[subject2] = marks2
marksheet[subject3] = marks3

print(marksheet)