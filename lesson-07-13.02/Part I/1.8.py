import re

def match(pattern: str, text: str):
    match = re.search(pattern, text)
    return True if match else False

text0 = "This is hello, World Test"
text1 = "hello, 322world"
text2 = "anitazhaniyaeva228"

pattern = "^[a-zA-Z0-9]+$"
pattern1 = "^\w+$"

print(match(pattern, text0))
print(match(pattern, text1))
print(match(pattern, text2))

print(match(pattern1, text0))
print(match(pattern1, text1))
print(match(pattern1, text2))