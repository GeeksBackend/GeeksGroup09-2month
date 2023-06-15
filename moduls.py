#1. импортировать сам модуль
# import lesson_8

# lesson_8.avg([1, 2, 3, 4, 5])
# lesson_8.reverse_word("Geeks")
# lesson_8.hello_student("Kurmanbek", "Islam", "Bayzak", "Nurbolot")

#2. импортировать отдельные определения из модуля
# from lesson_8 import avg, reverse_word

# avg((10, 20, 30, 40, 50))
# avg((2, 2, 2, 3, 3, 3, 4, 5))
# reverse_word("Kurmanbek")

#3. импортировать всё содержимое модуля сразу
from lesson_8 import *

avg((2, 2, 2, 3, 3))
reverse_word("Bayzak")
hello_student("Kurmanbek", "Robert", "Nurbolot")
avg((10, 20, 30, 40, 40, 40))
print(it)