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
print_models(unprinted_designs, completed_models)

# Call the function to show completed models
show_completed_models(completed_models)