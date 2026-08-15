from pathlib import Path

path = Path('large_pi_digit.txt')
contents = path.read_text()
contents = contents.splitlines()
pi_string = ''
for line in contents:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form of mmddyy: ")
if birthday in pi_string:
    print("Congratulations! Your birthday appear in first million digits of PI.")
else:
    print("Sorry! Your birthday doesn't appear in first million digits of PI.")