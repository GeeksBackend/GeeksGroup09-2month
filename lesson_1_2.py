#ООП - Объектно-ориентированное программирование
# class Car(): 
#     brand = "Toyota" #Атрибут (свойства) brand с значением Toyota
#     model = "Prius" #Атрибут (свойства) model с значением Prius

#     def drive(self): #Метод drive внутри класса Car
#         #self - это стандартное имя первого аргумента для создания методов
#         print("Drive Car") #Выводим значение Drive Car

#     def stop_car(self): #Метод stop_car 
#         print("Stop Car") #Выводим значение Stop Car

# car = Car() #Объект или экземпляр класса Car
# print(car)
# print(car.brand) #Вызывем атрибут brand с класса Car
# print(car.model) #Вызывем атрибут model с класса Car
# car.drive() #Вызываем метод drive через объект класса car (10 line)
# car.stop_car() #Вызываем метод stop_car через объект класса car (10 line)

# def welcome(name:str) -> str:
#     return f"Welcome {name}"
# print(welcome("Kurmanbek"))

class Airplane: #Динамический класс Airplane
    def __init__(self, name, passenger_seats, weight): #Конструктор
        self.name = name
        self.passenger_seats = passenger_seats
        self.weigth = weight
        self.odometer = 0
        self.is_flying = False

    def info(self):
        return f"{self.name}, {self.passenger_seats}, {self.weigth} {self.odometer}km, {self.is_flying}"
    
    def fly(self):
        if self.is_flying == False:
            self.is_flying = True 
            return f"Начинаем взлет самолета {self.name}"
        else:
            return f"У вас уже заведен двигатель"
    
    def flying(self, km):
        if self.is_flying == True:
            self.odometer += km 
            return f"Вы пролетели на самолете {self.name}, {km} km"
        else:
            return "У вас отключены двигатели"
    
    def landing(self):
        if self.is_flying == True:
            self.is_flying = False 
            return f"Вы сделали посадку самолета, двигатели отключены"
        else:
            return "Вы не можете сделать посадку так как вы уже на землеы"

boeing_747 = Airplane("Boeing 747", 660, 183500)
print(boeing_747.info())
print(boeing_747.fly())
print(boeing_747.flying(300))
print(boeing_747.info())
print(boeing_747.flying(300))
print(boeing_747.info())
print(boeing_747.landing())
print(boeing_747.info())
print(boeing_747.flying(300))
