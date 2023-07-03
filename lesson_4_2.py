#Магические методы
# class Student:
#     def __init__(self, name, surname, age):
#         self.name = name 
#         self.surname = surname 
#         self.age = age 
#         self.books = []
#         self.knowledge = 0

#     def __str__(self):
#         return f"{self.name} {self.surname} {self.knowledge} {self.books}"
    
#     def read_book(self, name_book):
#         self.books.append(name_book)
#         self.knowledge += 100
#         return f"Ученик {self.name} прочитал книгу и получил 100 баллов"
    
#     def __eq__(self, other):
#         return other.knowledge == self.knowledge
    
#     def __gt__(self, other):
#         return self.knowledge > other.knowledge
    
#     def __lt__(self, other):
#         return self.knowledge < other.knowledge

# beksultan = Student('Beksultan', 'Nurlan Uulu', 18)
# print(beksultan)
# print(beksultan.read_book('Python для чайников'))
# print(beksultan)
# print("====================")
# nurbolot = Student('Nurbolot', 'Erkinbaev', 18)
# print(nurbolot)
# print(nurbolot.read_book('Грокаем алгоритмы'))
# print(nurbolot.read_book('Чистый код'))
# print(nurbolot)
# print("############################")
# print(beksultan == nurbolot)
# print(beksultan > nurbolot)
# print(beksultan < nurbolot)

import sqlite3
import random

connection = sqlite3.connect('bank.db')
cursor = connection.cursor() #После создания объекта соединения с базой данных нужно создать объект cursor. Он позволяет делать SQL-запросы к базе. Используем переменную cursor для хранения объекта

cursor.execute("""CREATE TABLE IF NOT EXISTS clients (
    name VARCHAR(100),
    surname VARCHAR(100),
    age INTEGER,
    balance INTEGER,
    wallet_id VARCHAR(50),
    email VARCHAR(255),
    password VARCHAR(100)
);
""") #Создаем таблицу clients для клиентов банка с колоннами name, surname, age, balance, wallet_id, email, password

class Bank:
    def __init__(self):
        self.name = None 
        self.surname = None 
        self.age = None 
        self.balance = None 
        self.wallet_id = None 
        self.email = None 

    def register(self, name, surname, age, email, password):
        cursor = connection.cursor()
        random_wallet_id = random.randint(11111111, 99999999)
        cursor.execute(f"""INSERT INTO clients (name, surname, age, balance, wallet_id, email, password) 
                       VALUES ('{name}', '{surname}', {age}, 0, '{random_wallet_id}', '{email}', '{password}');""")
        cursor.connection.commit()
        print(f"Уважаемый {name} {surname} вы успешно создали счет в нашем банке")

    def authorization(self, email, password):
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM clients WHERE email = '{email}' AND password = '{password}';")
        result = cursor.fetchall()
        if result == []:
            print("Неправильный логин или пароль")
        else:
            self.name = result[0][0]
            self.surname = result[0][1]
            self.age = result[0][2]
            self.balance = result[0][3]
            self.wallet_id = result[0][4] 
            self.email = result[0][5]
            print(f"{self.name} {self.surname} вы успешно авторизовались") 

    def get_info(self):
        if self.name and self.surname:
            print(f"Информация:\nИмя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}, Баланс {self.balance} KGS, ID кошелька {self.wallet_id}, Почта: {self.email}")
        else:
            print("Вы не авторизованы")

    def top_up_balance(self, amount):
        if self.name and self.surname:
            if amount <= 5000:
                self.balance += amount
                cursor.execute(f"UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}';")
                cursor.connection.commit()
                print(f"{self.name} {self.surname} вы успешно попонили свой баланс на {amount} KGS")
            else:
                print("За одну операцию можно пополнять свой счет на 5000 KGS")
        else:
            print("Вы не авторизованы")

    def money_transfer(self, wallet_id, amount):
        if self.name and self.surname:
            cursor.execute(f"SELECT * FROM clients WHERE wallet_id = '{wallet_id}';")
            res = cursor.fetchall()
            if res != []:
                if self.balance >= amount:
                    self.balance -= amount
                    cursor.execute(f"UPDATE clients SET balance = balance - {amount} WHERE email = '{self.email}';")
                    cursor.execute(f"UPDATE clients SET balance = balance + {amount} WHERE wallet_id = '{wallet_id}';")
                    cursor.connection.commit()
                    print("Перевод успешно совершен")
                else:
                    print("Вы не можете перевести больше чем ваш текущий баланс")
            else:
                print("ID счета не найден")
        else:
            print("Вы не авторизованы")

    def main(self):
        while True:
            command = input("1 - регистрация, 2 - авторизация, 3 - информация, 4 - пополнить, 5 - вывести, 6 - перевести: ")
            if command == "1":
                name = input("Имя: ")
                surname = input("Фамилия: ")
                age = int(input("Возраст: "))
                email = input("Почта: ")
                password = input("Введите пароль: ")
                self.register(name, surname, age, email, password)
            elif command == "2":
                email = input("Почта: ")
                password = input("Пароль: ")
                self.authorization(email, password)
            elif command == "3":
                self.get_info()
            elif command == "4":
                amount = int(input("Сколько: "))
                self.top_up_balance(amount)
            elif command == "6":
                wallet_id = input('ID счета: ')
                amount = int(input("KGS: "))
                self.money_transfer(wallet_id, amount)

optima = Bank()
optima.main()