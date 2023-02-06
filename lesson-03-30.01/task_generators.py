# 1 4 9 16

def generator(n: int):
    for i in range(1, n):
        yield i ** 2

a = generator(5)
print(type(a))
for i in a:
    print(i, end=" ")