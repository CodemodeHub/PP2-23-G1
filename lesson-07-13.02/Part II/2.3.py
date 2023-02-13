import re

def check_python(text):
  pattern = "^[a-zA-Z1-9_]+$"
  result = re.search(pattern, text)
  return result != None

print(check_python("anita_zhaniyA_Eva"))
print(check_python("I love programming with Python"))
print(check_python("I love programming Python with Python"))