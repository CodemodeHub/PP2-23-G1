import re

def check_python(text):
  pattern = "[0-9]{2}/[0-9]{2}/[0-9]{4}"
  result = re.search(pattern, text)
  return result != None

print(check_python("anita_zhaniyA_Eva"))
print(check_python("I love programming with Python"))
print(check_python("13/02/2023"))