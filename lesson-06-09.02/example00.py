import re

pattern = re.compile("[\Da-zA-Z]+")
text = "123The quick brown fox123 jumps over the lazy dog."
matches = pattern.findall(text)

print(matches)