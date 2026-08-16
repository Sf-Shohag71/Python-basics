from pathlib import Path
import json

numbers = [2, 5, 2, 6, 3, 9, 10]
path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)