import re

def match(pattern: str, text: str):
    match = re.search(pattern, text)
    return True if match else False

text0 = "This is hello, World Test"
text1 = "hello, 322world"
text2 = "anitazhaniyaeva228"
text3 = "https://www.test.com"

pattern = "^https://www.[a-z]+.com"

print(match(pattern, text0))
print(match(pattern, text1))
print(match(pattern, text2))
print(match(pattern, text3))

