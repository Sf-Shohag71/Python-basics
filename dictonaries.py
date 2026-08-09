# person = {
#     'first_name': 'sanjoy',
#     'last_name': 'Roy',
#     'age': 27,
#     'city': 'Dinajpur'
# }
# print(f"First Name: {person['first_name']}\nLast Name: {person['last_name']}\nAge: {person['age']}\nCity: {person['city']}")

# favorite_numbers = {
#     'sanjoy': 7,
#     'shohag': 3,
#     'alif': 5,
#     'rakib': 9
# }
# print(f"Sanjoy's favorite number is {favorite_numbers['sanjoy']}. His from {person['city']}.")
# print(f"Shohag's favorite number is {favorite_numbers['shohag']}.")


# Loop through both keys and values
# user_info = {"name": "Alice", "age": 30, "city": "Dhaka"}

# for key, value in user_info.items():
#     print(f"Key: {key} | Value: {value}")


# # Loop through keys directly
# user_info = {"name": "Alice", "age": 30, "city": "Dhaka"}

# for key in user_info:
#     value = user_info[key]  # Access value using the key
#     print(f"Key: {key} | Value: {value}")


favorite_language = {
    'sarah' : 'python',
    'shohag' : 'javascript',
    'phil' : 'c'
}

friends = ['shohag', 'sarah']
for name in favorite_language:
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_language[name].title()
        print(f"\t{name.title()}, I see you love {language}!")