import re

pattern = "\d+"
pattern_digits = "[1-9]+"
pattern_digits_none = "\D+"
text = "The quick brown fox jumps over the lazy dog 12a3."

matches = re.findall(pattern, text)
matches1 = re.findall(pattern_digits, text)
matches2 = re.findall(pattern_digits_none, text)

print(matches)
print(matches1)
print(matches2)