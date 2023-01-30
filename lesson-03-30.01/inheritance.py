class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def sayHello(self):
        print(f"{self.name}: Hello!")

class Student(Person):
    def __init__(self, name: str, age: int, id: str):
        super().__init__(name, age)
        self.id = id
    
    def passExam(self):
        print("Exam")

p = Person("Alikhan", 19)
p.sayHello()

s = Student("Anita", 18, "21B0123")
s.sayHello()