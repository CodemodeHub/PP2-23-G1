n, m = map(int, input().split())

arr = []

for i in range(0, n):
    tmp = []
    for j in range(0, m):
        tmp.append(int(input()))
    arr.append(tmp)

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

for i in range(0, n):
    for j in range(0, m):
        print(arr[i][j], end=" ")
    print()