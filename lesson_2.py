# print("Hello Geeks and Python") #Выводит слово
"""Это многострочный комментарий
Python будет игнорировать
данный текст"""

# str_example_1 = 'Hello, I\'m backend developer'
# print(str_example_1)

# str_example_2 = "Hello, I'm backend developer\nLanguage Python"
# print(str_example_2)

# str_example_3 = """Hello, I'm backend developer
# Language Python"""
# print(str_example_3)

# str_example_4 = '''Hello, I'm backend developer
# Language Python'''
# print(str_example_4)

#Конкантенация - это склеивание строк через оператор +
# print("Nurbolot" + " " + 'Erkinbaev')
# print("Nurbolot " + "Erkinbaev")
# print("Nurbolot", 'Erkinbaev')

# name = input("Имя: ")
# print("Привет", name)

# it = "Geeks " #Индексы строк
#      #012345 
# print(it[3])
# print(it[0])
# print(it[5])

# print(it[0:4])

# language = "Python"
#            #012345
# print(language[0:2])
# print(language[::2])

# name = "nurBOloT"
# print(name.title())
# print(name.upper())
# print(name.lower())

#Условия if, elif, else
# num1 = 100
# num2 = 50
# if num1 > num2:
#     print("Переменная num1 больше")
# else:
#     print("Переменная num2 больше")

#Операторы сравнения (6)
# print(30 == 30)
# print(40 == 10)

# print(20 != 5)
# print(10 != 10)

# print(30 > 3)
# print(30 > 100)

# print(40 < 4)
# print(40 < 40)

# print(40 <= 40)
# print(40 <= 100)

# print(50 >= 100)
# print(60 >= 60)

# age = int(input("Ваш возраст: "))
# if age < 14:
#     print("Извините, ваш возраст не подходит")
# else:
#     print("Добро пожаловать на курсы Geeks!")

# login = input("Login: ")
# password = input("Password: ")
# if login == "geeks" or password == "geeksstudents":
#     print("Welcome")
# else:
#     print("Error")

num1 = 1000
num2 = 1000
num3 = 1000
if num1 > num2 and num1 > num3:
    print('num1 больше')
elif num2 > num1 and num2 > num3:
    print('num2 больше')
elif num3 > num1 and num3 > num2:
    print('num3 больше')
else:
    print("Они все равны")