# prompt = "\nGive me any text and I will repeat it back to you."
# prompt += "\nType 'exit' to end the program. "

# message = ""
# while message != 'exit':
#     message = input(prompt).lower()
#     print(message)

# Finding odd numbers in a range of numbers 1-20
# current_number = 0
# while current_number < 20:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# Finding movie ticket prices
# prompt = "\nPlease enter your age (or type 'quit' to exit): "
# active = True

# while active:
#     age_input = input(prompt)
#     if age_input.lower() == 'quit':
#         active = False
#         continue
#     else:
#         age = int(age_input)

#         if age < 3:
#             print("Your ticket is free!")
#         elif age <=12:
#             print("Your ticket cost $10.")
#         else:
#             print("Your ticket cost $15")


# Verifiying user 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nConfirmed users:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())