#Магические методы
class Student:
    def __init__(self, name, surname, age):
        self.name = name 
        self.surname = surname 
        self.age = age 
        self.books = []
        self.knowledge = 0

    def __str__(self):
        return f"{self.name} {self.surname} {self.knowledge} {self.books}"
    
    def read_book(self, name_book):
        self.books.append(name_book)
        self.knowledge += 100
        return f"Ученик {self.name} прочитал книгу и получил 100 баллов"
    
    def __eq__(self, other):
        return other.knowledge == self.knowledge
    
    def __gt__(self, other):
        return self.knowledge > other.knowledge
    
    def __lt__(self, other):
        return self.knowledge < other.knowledge

beksultan = Student('Beksultan', 'Nurlan Uulu', 18)
print(beksultan)
print(beksultan.read_book('Python для чайников'))
print(beksultan)
print("====================")
nurbolot = Student('Nurbolot', 'Erkinbaev', 18)
print(nurbolot)
print(nurbolot.read_book('Грокаем алгоритмы'))
print(nurbolot.read_book('Чистый код'))
print(nurbolot)
print("############################")
print(beksultan == nurbolot)
print(beksultan > nurbolot)
print(beksultan < nurbolot)