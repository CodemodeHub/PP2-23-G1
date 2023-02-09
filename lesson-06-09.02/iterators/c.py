class SquaredElements:
    def __init__(self, lst):
        self.lst = lst
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= len(self.lst):
            raise StopIteration
        value = self.lst[self.current] ** 2
        self.current += 1
        return value

squared_elements = SquaredElements([1, 2, 3, 4, 5])
for number in squared_elements:
    print(number, end=" ")