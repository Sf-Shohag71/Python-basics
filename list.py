# Python crash course page - 41
guest_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print(f"Hello {guest_list[0]}, you are invited to dinner.")
print(f"Hello {guest_list[1]}, you are invited to dinner.")
print(f"Hello {guest_list[2]}, you are invited to dinner.")
print(f"\nGuest list: {guest_list}")

# this guest can't make it, so we need to replace them with someone else
print(f"\nUnfortunately, {guest_list[2]} can't make it to dinner.")
guest_list[2] = 'Frank'
print(f"\nHello {guest_list[0]}, you are invited to dinner.")
print(f"Hello {guest_list[1]}, you are invited to dinner.")
print(f"Hello {guest_list[2]}, you are invited to dinner.")
print(f"Hello {guest_list[3]}, you are invited to dinner.")
print(f"Hello {guest_list[4]}, you are invited to dinner.")

# New guest list
print(f"\nNew guest list: {guest_list}")
print("Good news! We found a bigger dinner table, so we can invite more guests.")

# Adding new guests beginning, middle and end of the list
guest_list.insert(0, 'Sanjoy')
guest_list.insert(3, 'Grace')
guest_list.append('Heidi')
print(f"\nHello {guest_list[0]}, you are invited to dinner.")
print(f"Hello {guest_list[3]}, you are invited to dinner.")
print(f"Hello {guest_list[-1]}, you are invited to dinner.")
print(f"\nUpdated guest list: {guest_list}")

# Removing guests until only four remain
print("\nUnfortunately, we can only invite four guests to dinner.")
cancelled_guest = guest_list.pop()
print(f"\nSorry {cancelled_guest}, we can't invite you to dinner.")
cancelled_guest = guest_list.pop()
print(f"\nSorry {cancelled_guest}, we can't invite you to dinner.")
cancelled_guest = guest_list.pop()
print(f"\nSorry {cancelled_guest}, we can't invite you to dinner.")
cancelled_guest = guest_list.pop()
print(f"\nSorry {cancelled_guest}, we can't invite you to dinner.")
print(f"\nUpdated guest list: {guest_list}. We can only invite four guests to dinner.")

# Removing guests until only one remains
del guest_list[-1]
del guest_list[-1]
del guest_list[-1]
del guest_list[-1]
print(f"\nFinal guest list: {guest_list}.")