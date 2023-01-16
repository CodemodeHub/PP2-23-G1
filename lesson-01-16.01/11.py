arr = list(map(int, input().split()))

evens = []
odds = []

for i in range(0, len(arr)):
    if arr[i] % 2 == 0:
        evens.append(arr[i])
    elif arr[i] % 2 == 1:
        odds.append(arr[i])
 
print(evens)
for num in evens:
    print(num, end=" ")

# print(odds)