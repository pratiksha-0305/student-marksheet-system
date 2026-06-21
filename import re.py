import re
text = "My number is 123"
result = re.findall(r"\d+", text)
print(result)