#Args, kwargs. Lambda функции
def students(name1, name2, name3):
    print("Привет", name1)
    print("Привет", name2)
    print("Привет", name3)
# students("Нурислам", "Нурболот", "Роберт")

def args_students(*names):
    # print(args)
    for name in names:
        print("Привет", name)
# args_students("Нурислам", "Нурболот", "Роберт", "Ислам", "Ажыбек")

def students_point(name:str, *points:int) -> str:
    print(name, sum(points) / len(points))
# students_point("Samat", 4, 4, 4, 4, 2, 2, 5)
# students_point("Islam", 4, 4, 4, 4, 5, )

def translate(**words):
    print(words)
# translate(USA="США", Apple="Яблоко", Car="Машина", Geeks="Гикс")

def add(num1:int=1, num2:int=1) -> int:
    print(num1 + num2)

def sub(num1:int=1, num2:int=1) -> int:
    print(num1 - num2)

def mult(num1:int=1, num2:int=1) -> int:
    print(num1 * num2)

def div(num1:int=1, num2:int=1) -> float:
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")

def main(number1:int=1, number2:int=1, operator:str="+") -> int:
    if operator == "+":
        add(number1, number2)
    elif operator == "-":
        sub(number1, number2)
    elif operator == "*":
        mult(number1, number2)
    elif operator == "/":
        div(number1, number2)
    else:
        print("Такого оператора нету. Используйте +, -, *, /")
# main(10, 30, "+")
# main(30, 30, "*")
# main(33, 40, "-")
# main(3, 0, "/")

#Lambda функции
# def hello(word):
#     print(word)
# hello("Geeks")

# lambda_hello = lambda word: word 
# print(lambda_hello("Geeks"))

# print((lambda word: word)("Geeks"))

#Пример 2
# def add(num1:int=1, num2:int=1):
#     print(num1 + num2)
# add(10, 30)

# lambda_add = lambda num1, num2: num1 + num2 
# print(lambda_add(10, 30))

# print((lambda num1, num2: num1 + num2)(10, 30))

#Пример 3
# f = lambda: True #Лямбда-функция без аргументов
# print(f())

#Пример 4
# numbers = [1, 2, 3, 4, 5, 6]
# new_numbers = []
# def mult_two(nums:list) -> list:
#     for n in nums:
#         new_numbers.append(n * 2)
#     print(new_numbers)
# mult_two(numbers)

# numbers = [1, 2, 3, 4, 5, 6]
# lambda_new_numbers = list(map(lambda nums: nums * 2, numbers))
# print(lambda_new_numbers)

# numbers = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda nums: nums * 2, numbers)))

# print(list(map(lambda nums: nums * 2, [1, 2, 3, 4, 5, 6])))

#Пример 5
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# chet = []
# def numbers_chet(nums:list) -> list:
#     for n in nums:
#         if n % 2 == 0:
#             chet.append(n)
#     print(chet)
# numbers_chet(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lambda_numbers_chet = list(filter(lambda nums: nums % 2 == 0, numbers))
# print(lambda_numbers_chet)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda nums: nums % 2 == 0, numbers)))

# print(list(filter(lambda nums: nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

from lesson_8 import reverse_word

reverse_word("Robert")