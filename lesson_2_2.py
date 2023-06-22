#Принципы ООП. Наследование, Полиморфизм, Инкапсуляция и Абстракция
# hello = ""
# lst = []
# def hello_world():
#     pass
# hello_world()

# class Hello:
#     pass 
# hello = Hello()

# class Person: #Родительский класс Person
#     def __init__(self, name, surname, age): #Конструктор класса
#         self.name = name #Динамический атрибут name
#         self.surname = surname #Динамический атрибут surname
#         self.age = age #Динамический атрибут age

#     def get_info(self): #Метод get_info
#         return f"{self.name} {self.surname} {self.age}"
    
# askhat = Person('Askhat', 'Kydyrov', 18) #Экземпляр класса Person
# print(askhat.get_info())

# class Bank(Person): #Дочерний класс Bank, которая наследуется от класса Person
#     def __init__(self, name, surname, age): #Конструктор класса Bank
#         super().__init__(name, surname, age) 
#         self.balance = 0 #Новый динамический атрибут balance с значением 0

#     def get_balance(self): #Новый метод get_balance
#         return f"{self.name}, balance {self.balance} KGS"

#     def top_up_balance(self, amount):
#         self.balance += amount
#         return f"{self.name}, ваш баланс пополнен на {amount} KGS"

#     def withdraw_money(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return f"{self.name}, вы сняли со своего счета {amount} KGS"
#         else:
#             return f"{self.name} недостаточно денег для вывода"

# askhat_bank = Bank('Askhat', 'Kydyrov', 18) #Экземпляр класса Bank
# print(askhat_bank.get_info()) #Вызываем метод get_info
# print(askhat_bank.get_balance()) #Вызываем метод get_balance
# print(askhat_bank.top_up_balance(1000))
# print(askhat_bank.get_balance())
# print(askhat_bank.withdraw_money(1000))
# print(askhat_bank.get_balance())

# class Work(Bank):
#     def __init__(self, name, surname, age, work):
#         super().__init__(name, surname, age)
#         self.work = work

#     def get_info(self): #Переопределение метода get_info
#         return f"Name: {self.name}, surname {self.surname}, age {self.age}, balance {self.balance}, work {self.work}"

# driver_askhat = Work('Askhat', 'Kydyrov', 18, 'Driver')
# print(driver_askhat.get_balance())
# print(driver_askhat.top_up_balance(2000))
# print(driver_askhat.get_balance())
# print(driver_askhat.get_info())

#Множественное наследование

# class A:
#     def class_a(self):
#         return f"Class A"
    
# class B:
#     def class_b(self):
#         return f"Class B"
    
# class C(A, B): #Множественное наследование
#     pass

# c = C()
# print(c.class_a())
# print(c.class_b())

class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer = 0
        self.fuel = 70

    def add_distance(self, km):
        self.odometer += km

    def subtract_fuel(self, amount):
        self.fuel -= amount

    def drive(self, km):
        if (self.fuel * 10) >= km:
            self.add_distance(km)
            self.subtract_fuel(km / 10)
            return f"Вы проехали {km} km, у вас осталось {self.fuel} литров бензина вы можете проехать еще {round(self.fuel * 10)} km"
        else:
            return "У вас недостаточно топлива для поездки"

camry = Car('Toyota', 'Camry 55', 2016)
print(camry.drive(60))
print(camry.fuel)