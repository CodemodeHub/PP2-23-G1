class UniqueElements:
    def __init__(self, lst):
        self.lst = list(set(lst))
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= len(self.lst):
            raise StopIteration
        value = self.lst[self.current]
        self.current += 1
        return value

unique_elements = UniqueElements([1, 2, 2, 3, 4, 4, 4, 5, 5])
for number in unique_elements:
    print(number)