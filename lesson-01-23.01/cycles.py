arr = [1, 2, 3]

for i in range(0, len(arr), 2):
    print(arr[i], end=" ")

print()

for i in range(0, len(arr)):
    print(arr[i], end=" ")

print()

for element in arr:
    print(element, end=" ")

print()

for (index, value) in enumerate(arr):
    print(index, " ", value)