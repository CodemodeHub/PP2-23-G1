import re

def match(pattern: str, text: str):
    match = re.search(pattern, text)
    return True if match else False

text0 = "This is hello, World Test"
text1 = "hello, world"

pattern = ".world$"

print(match(pattern, text0))
print(match(pattern, text1))