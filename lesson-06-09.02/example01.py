import re

def match_string(string):
    pattern = '^a[b]{3}'
    result = re.match(pattern, string)
    return True if result else False

print(match_string("ab"))
print(match_string("abbb"))
print(match_string("ba"))
print(match_string("ac"))