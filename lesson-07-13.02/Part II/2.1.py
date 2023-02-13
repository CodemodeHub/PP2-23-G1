import re

def check_python(text):
  pattern = "Python"
  result = re.search(pattern, text)
  return result != None

print(check_python("Python is an interpreted, high-level, general-purpose programming language."))
print(check_python("I love programming with Python"))
print(check_python("I love programming Python with Python"))