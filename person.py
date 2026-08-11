def build_person(first_name, last_name):
    """Build a dictionary containing information about a person."""
    person = {'first_name': first_name, 'last_name': last_name}
    return person

person = build_person('John', 'Doe')
# print(person)

def build_person_with_age(first_name, last_name, age=None):
    """Build a dictionary containing information about a person, including age if provided."""
    person = {'first_name': first_name, 'last_name': last_name}
    if age is not None:
        person['age'] = age
    return person

person_with_age = build_person_with_age('John', 'Doe', 30)
# print(person_with_age)
# print(person_with_age)

# list of people in a function
# def build_people_list(names):
#     for name in names:
#         print(f"\nHello, {name.title()}!")

# build_people_list(['alice', 'bob', 'charlie'])

# printing a list of models
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the function to print models
# print_models(unprinted_designs, completed_models)

# Call the function to show completed models
# show_completed_models(completed_models)

# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza(12, 'pepperoni', 'mushrooms', 'green peppers')

# Mixing positional and arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)