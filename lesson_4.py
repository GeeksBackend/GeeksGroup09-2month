#Циклы for и while
# print("Hello World 1")
# print("Hello World 2")
# print("Hello World 3")
# print("Hello World 4")
# print("Hello World 5")
# print("Hello World 6")
# print("Hello World 7")

# for i in range(100001):
#     print("Hello World", i)

# for n in range(1001):
#     print(n)
#     print("Geeks")

# for day in range(1, 32):
#     print("Утро")
#     print("День", day)
#     print("Ночь")
#     print("==============")

# number = int(input("Number: "))
# if number % 2 == 0:
#     print(number, "четный")
# else:
#     print(number, "нечетный")

# chet_numbers = []
# for numbers in range(2, 101, 2):
#     chet_numbers.append(numbers)
# print(chet_numbers)

# numbers = [10, 11, 13, 1001, 1002, 1010, 3, 4, 66, 88, 90, 103, 507, 809, 104, 1016]
# chet = []
# for num in numbers: #Итерация списка numbers
#     if num % 2 == 0:
#         chet.append(num)
# print(chet)

# names = ["Kurmanbek", "Janysh", "Nurbolot", "Asylbek", "Askhat"]
# print(names)
# for name in names:
#     print(name)
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])

# num1 = 10
# num2 = 30
# while num1 < num2:
#     num1 += 1
    # num1 = num1 + 1
    # print(num1)

# shet = 0
# while True:
#     shet += 1000
#     print(shet)
    #CTRL + C

# n = 0
# while True:
#     n += 10
#     print(n)
#     if n == 100000:
#         print("HACKED!!!")
#         break

# import time

# k = 0
# while True:
#     k += 10
#     print("HACK", k, "%")
#     if k == 100:
#         print("HACK SYSTEM")
#         break
#     time.sleep(5)

# import random

# # print(random.randint(1, 10))

# random_number = random.randint(1, 10)
# attempts = 3
# while True:
#     user_number = int(input("Введите число с 1 до 10: "))
#     if user_number >= 1 and user_number <= 10:
#         attempts -= 1
#         if user_number == random_number:
#             print("WIN!!!")
#             break 
#         elif attempts == 0:
#             print("LOSE!!!")
#             break
#         else:
#             print("WRONG ANSWER", attempts, "attempsts")
#     else:
#         print("Только число с 1 до 10")

# print("0", 1)
# print("0", 2)
# print("0", 3)
# print("0", 4)
# print("0", 5)