from name import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""

    formatted_name = get_formatted_name('janis', 'joplin')

    assert formatted_name == 'Janis Joplin'

# Run test for three arguments first, middle, and last name
def test_first_middle_last_name():
    """Do name like 'shakh farid shohag' work?"""
    formatted_name = get_formatted_name('shakh', 'shohag', 'farid')
    assert formatted_name == 'Shakh Farid Shohag'