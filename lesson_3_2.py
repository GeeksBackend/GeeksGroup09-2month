#Инкапсуляция
#Python предоставляет 3 уровня доступа к данным
#1 - public, 2 - protected (_), 3 - private (__)

# class Phone:
#     def __init__(self, brand, model, year, color):
#         self.brand = brand 
#         self.model = model 
#         self.year = year
#         self.color = color 
#         self.__phone_number = '0555667788'
#         self.__balance = 0
    
#     def get_info(self):
#         return f"Brand: {self.brand}, model {self.model}, year: {self.year}, color: {self.color}"
    
#     def get_phone_number(self):
#         return f"Ваш номер телефона {self.__phone_number}"
    
#     def get_balance(self):
#         return f"Ваш баланс телефона {self.__balance}"
    
#     def __balance_up(self, amount):
#         self.__balance += amount

#     def top_up_balance(self, amount):
#         self.__balance_up(amount)
#         return f"Вы пополнили свой баланс на {amount} сом"

# iphone_14_pro_max = Phone('Iphone', '14 PRO MAX', 2023, 'Black')
# print(iphone_14_pro_max.get_info())
# print(iphone_14_pro_max.get_phone_number())
# print(iphone_14_pro_max.get_balance())
# iphone_14_pro_max.__balance = 1000
# print(iphone_14_pro_max.get_balance())
# print(iphone_14_pro_max.top_up_balance(200))
# print(iphone_14_pro_max.get_balance())
# iphone_14_pro_max.__phone_number = '0777777777'
# print(iphone_14_pro_max.get_phone_number())

# class Bank:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname 
#         self.__balance = 0

#     def get_info(self):
#         return f"Name: {self._name}, surname: {self._surname}, {self.__balance} KGS"
    
# beksultan = Bank('Beksultan', 'Uraiumov')
# print(beksultan.get_info())
# beksultan._surname = "Nurlan Uulu"
# print(beksultan.get_info())
# beksultan.__balance = 10000
# print(beksultan.get_info())

# class Geeks(Bank):
#     pass 

# geeks = Geeks('Kurmanbek', 'Toktorov')
# print(geeks._name)  
# print(geeks._surname)
# print(geeks.__balance)

#Полиморфизм
# num1 = 10
# num2 = 20
# print(num1 + num2)

# geek = "Geek"
# studio = "Studio"
# print(geek + studio)

# print(len('Geeks'))
# print(len([10, 20, 30, 40]))
# print(len((40, 30, 20, 10, 5)))

# class Cow:
#     def make_sound(self):
#         return "Muuu"
    
# class Dog:
#     def make_sound(self):
#         return "Gawww"
    
# class Cat:
#     def make_sound(self):
#         return "Meow"
    
# cow = Cow()
# dog = Dog()
# cat = Cat()

# for animal in (cow, dog, cat):
#     print(animal.make_sound())