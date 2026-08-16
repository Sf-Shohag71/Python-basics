from pathlib import Path

filenames = ['cats.txt', 'dogs.txt', 'cows.txt']
for filename in filenames:
    print(f"\nReading file: {filename}")
    path = Path(filename)

    try:
        contents = path.read_text()
    except FileNotFoundError:
        # print(f"Sorry we couldn't find this file: {filename}")
        pass
    else:
        print(contents)