import re

pattern = "lines$"
text = "This is a string with multiple lines"

result = re.search(pattern, text, re.MULTILINE)
print(result)
