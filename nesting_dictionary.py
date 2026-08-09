# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese']
# }

# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"- {topping}")

favorite_languages = {
    'shohag' : ['python', 'c++'],
    'sanjoy' : ['java', 'c#'],
    'siam' : ['c++'],
    'rakib' : ['python', 'java', 'c#']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
