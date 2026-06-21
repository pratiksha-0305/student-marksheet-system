import re

text = input("Enter numbers: ")

odd_numbers = re.findall(r'\b\d*[13579]\b', text)

print("Odd numbers:", odd_numbers)