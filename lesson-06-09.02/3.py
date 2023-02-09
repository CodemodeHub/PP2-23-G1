import re

pattern = "[a-zA-Z]+"
text = "The quick brown fox jumps over the lazy dog."
matches = re.findall(pattern, text)
print(matches)

# Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']