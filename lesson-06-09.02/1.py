import re

text = "The quick brown fox jumps over the lazy dog."
word = "fox"

match = re.search(word, text)

if match:
    print("Found", match.group())
else:
    print("Not found")