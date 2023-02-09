import re

text = "The quick brown fox jumps over the lazy dog."
new_text = re.sub("fox", "cat", text)
print(new_text)

# Output: The quick brown cat jumps over the lazy dog.