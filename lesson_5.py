#Множества (set, frozenset)
#str, int, bool, list, tuple, float
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# print(set(a + b))

# st = {'Geeks', 'Osh', 'Bishkek', 'IT', 'Osh'}
# print(st)
# st.add('Asus')
# print(st)
# st.add("IT")
# print(st)
# st.remove("Bishkek")
# print(st)
# st.pop()
# print(st)
# st.clear()
# print(st)

# emails = {'geeks@gmail.com'}
# print(emails)
# emails.add('kurmanbek92@gmail.com')
# print(emails)
# emails.add('Geeks@gmail.com')
# print(emails)
# emails.add(1)
# emails.add("1")
# print(emails)

# frzn = frozenset({1, 1, 2, 2, 3, 4})
# print(frzn)
# frzn.remove(1)

#Словари - dictionary
# student = {'name':'Askhat', 'age':19, 'phone_number':996777123432}
# print(student)
# print(student['name'])
# #JSON
# print(student['phone_number'])
# print(len(student))
# student.setdefault('language', 'Python')
# print(student)
# student.pop('phone_number')
# print(student)
# student['age'] = 20
# print(student)
# print(student.keys())
# print(student.values())

contacts = {'MCHS':112}
while True:
    commands = input("1-посмотреть, 2-добавить, 3-удалить, 4-обновить: ")
    if commands == "1":
        print(contacts)
    elif commands == "2":
        add_name = input("Имя которую нужно добавить: ")
        if add_name in contacts:
            print("Такой контакт уже существует")
        else:
            add_number = input("Номер телефона: ")
            contacts.setdefault(add_name, add_number)
            print(f"Контакт {add_name} успешно добавлен")
    elif commands == "3":
        delete_name = input("Имя которую нужно удалить: ")
        if delete_name in contacts:
            contacts.pop(delete_name)
            print(f"Контакт {delete_name} успешно удален")
        else:
            print("Такого контакта нету")
    elif commands == "4":
        update_number = input("Кого нужно обновить? ")
        if update_number in contacts:
            new_numbers = input("Новый номер: ")
            contacts[update_number] = new_numbers
            print(f"Контакт {update_number} успешно обновлен")
        else:
            print("Такого контакта нету")

