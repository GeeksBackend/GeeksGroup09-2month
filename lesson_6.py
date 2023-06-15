#Functions - функции
# print()
# len()
# input()
#Это встроенные функции

# print("Hello Geeks")
# def hello(): #Пользовательская функция hello. Создается с помощью оператора def
#     print("Hello World")
#     print("Geeks")
# hello()

# def welcome():
#     name = input("Name: ")
#     print(f"Welcome {name}!")
    # print("Welcome", name, "!")
    # print("Welcome " + name + "!")
# welcome()

# def calculator():
#     num1 = int(input("Number1: "))
#     operator = input("+, -, *, /: ")
#     num2 = int(input("Number2: "))
#     if operator == "+":
#         print(f"Result {num1 + num2}")
#     elif operator == "-":
#         print(f"Result {num1 - num2}")
#     elif operator == "*":
#         print(f"Result {num1 * num2}")
#     elif operator == "/":
#         print(f"Result {num1 / num2}")
#     else:
#         print("Error operator")
# # calculator()

# def add(num1, num2): #num1, num2 являются параметрами функции add
#     print(num1 + num2)
# add(10, 20) #Значение 10 и 20 являются аргументами
# add("10", "20")

# def mult(num1:int, num2:int):
#     print(num1 * num2)
# mult(10, 20)
# mult("Geeks", 3)

# def sub(num1:int, num2:int) -> int:
#     print(num1 - num2)
# sub(20, 10)

# def div(num1:int=1, num2:int=1) -> float:
#     "Данная функция принимает два числа и делит их"
#     print(num1 / num2)
# div()
# div(20)

# import random

# def generator_password(len_password:int=8) -> str:
#     letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
#     result = ""
#     for n in range(len_password):
#         random_letter = random.choice(letters)
#         result += random_letter
#     print(result)
# generator_password(20)
# generator_password(4)
# generator_password(15)

#Иключения try, except
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")

# try:
#     print("10" + 10)
# except TypeError:
#     print("Ошибка типов данных")

# def calculator(num1:int=1, operator:str="+", num2:int=1):
#     try:
#         if operator == "+":
#             print(f"Result {num1 + num2}")
#         elif operator == "-":
#             print(f"Result {num1 - num2}")
#         elif operator == "*":
#             print(f"Result {num1 * num2}")
#         elif operator == "/":
#             try:
#                 print(f"Result {num1 / num2}")
#             except ZeroDivisionError:
#                 print("Деление на ноль!")
#             except TypeError:
#                 print("Ошибка деления проверьте что num1 и num2 integer")
#         else:
#             print("Error operator")
#     except:
#         print("Ошибка")
# calculator(20, "+", 20)
# calculator(10, "/", 0)
# calculator("Hello", "-", "World")

# raise ValueError("Hello Geeks")