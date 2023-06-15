# def hello_student(*names):
#     for name in names:
#         print("Привет", name)

# def avg(object:list) -> int:
#     "Вычисляет среднее арифметическое значение из списка и кортежей"
#     print(sum(object) / len(object))

# def reverse_word(word:str) -> str:
#     "Переворачивает строку"
#     print(word[::-1])

# it = "Geeks"

#Работа с файлами
# f = open('geeks.txt', 'w')
# f.write("Hello Geeks Backend 09!")
# f.close()

# r = open('geeks.txt', 'r')
# print(r.read())
# r.close()

# py = open('hello.py', 'w')
# py.write("print('Hello World')")
# py.close()

# read_py = open('lesson_2.py', 'r', encoding='utf-8')
# print(read_py.read())
# read_py.close()

# import os 
# os.remove("C:/Users/user/Desktop/geeks/hello.txt")
# os.rmdir("C:/Users/user/Desktop/geeks")
# os.mkdir("C:/Users/user/Desktop/gggggggg")

# import os 

# n = 0
# while True:
#     n += 1
#     os.mkdir(f"C:/Users/user/Desktop/test/hello{n}")
#     if n == 1000:
#         break

with open('hello.txt', 'w') as hello:
    hello.write("Hello World")

with open('hello.txt', 'r') as read_file:
    print(read_file.read())

with open('rus.txt', 'w', encoding='utf-8') as rus:
    rus.write("Привет мир и гикс!")

with open('students.txt', 'w', encoding='utf-8') as student:
    student.write("Islam\n")
    student.write("Robert\n")

with open('students.txt', 'a', encoding='utf-8') as new_student:
    new_student.write("Nurbolot\n")