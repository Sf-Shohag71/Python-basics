from pathlib import Path

def count_word(path, word):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, {path} does not found")
    else:
        line = contents.lower().count(word)
        print(f"The {path} have the word 'the': {line} ")


filenames = ['moby_dick.txt', 'little_women.txt', 'alice.txt', 'cows.txt']
for filename in filenames:
    path = Path(filename)
    count_word(path, 'the ')