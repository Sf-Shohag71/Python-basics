# dimantions = (200, 300)
# for dimantion in dimantions:
#     print(dimantion)

# dimantions = (400, 500)
# for dimantion in dimantions:
#     print(dimantion)

# print(dimantions)

# banned_users = ["alice", "bob", "charlie"]
# user = "shohag"

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")


available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"adding {requested_topping}.")
    else:
        print(f"sorry, we don't have {requested_topping}.")

print("\nHere is your pizza")