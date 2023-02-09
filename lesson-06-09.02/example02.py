import re

def match_abbs(string):
    pattern = '^ab{2,4}'
    match = re.match(pattern, string)
    return True if match else False

print(match_abbs("ab")) 
print(match_abbs("abb"))
print(match_abbs("abbb")) 
print(match_abbs("cabbbb")) 
print(match_abbs("abbbb")) 