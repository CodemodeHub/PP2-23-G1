class Person:
    def __init__(self, name: str):
        self.name = name

    def getName(self):
        return self.name

p = Person("Alikhan")
print(p.name)
print(p.getName())

# class Snake:
#     def __init__(self) -> None:
#         self.x = 0
#         self.y = 0
    
#     def moveUP(self, x):
#         self.x += x