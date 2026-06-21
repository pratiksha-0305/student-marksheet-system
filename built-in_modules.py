import sys
print(sys.version)
#print(sys.argv) #Agrument vector
sys.exit(0)




from collections import Counter
text = "apple banana apple"
words = text.split()
print(Counter(words))

import json
person = {"name": "John", "age": 20}
json_data = json.dumps(person)
print(json_data)

import re
text = "My number is 123"
result = re.findall(r"\d+", text)
print(result)

import string
print(string.ascii_uppercase)

from itertools import count
c = count(1)
print(next(c))
print(next(c))
print(next(c))

from pathlib import Path
path = Path("sample.txt")
print(path.name)