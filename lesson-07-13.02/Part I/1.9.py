import re

def match(pattern: str, text: str):
    match = re.search(pattern, text)
    return True if match else False

text0 = "This is hello, World Test"
text1 = "ahello, 322world"
text2 = "anitazhaniyaeva228z"
text3 = "abcz"

pattern = "^a.*.z$"

print(match(pattern, text0))
print(match(pattern, text1))
print(match(pattern, text2))
print(match(pattern, text3))