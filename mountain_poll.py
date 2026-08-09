responses = {}
active = True

while active:
    # prompt the user for their name and response
    name = input("\nWhat is your name? ")
    response = input(f"\nWhich mountain would you like to climb sometime in the future, {name}? ")

    # Store the response in the dictionary
    responses[name] = response

    # Ask if anyone else wants to respond
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        active = False

# Display the results of the poll
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

