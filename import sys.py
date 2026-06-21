import sys
print(sys.version)
#print(sys.argv) #Agrument vector
sys.exit(0)

import random
print(random.randint(1, 10))  # Random number from 1 to 10

import os
print(os.getcwd())  # Current folder

import time
print("Start")
time.sleep(2)  # Wait 2 seconds
print("End")

import calendar
print(calendar.month(2026, 5))

import statistics
numbers = [10, 20, 30, 40]
print(statistics.mean(numbers))

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