even_numbers = list(range(2, 11, 2))
# print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

# print(squares)

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")