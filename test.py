def func():
    a = input("Ведите фразу: ")
    isa = a.split()

    s = ''.join(i[0].upper() for i in isa)
    print(s)
func()

def func():
    text = """Money, money, money, it’s always sunny, in
    the richmen’s world"""
    print(text.count("money"))

func()

def reverse_number(n):
    num_str = str(n)

    reversed_str = num_str[::-1]

    reversed_num = int(reversed_str)

    return reversed_num

n = 27
reversed_n = reverse_number(n)
print(reversed_n) 
  
def chat_bot():
    while True:
        user_input = input("Ваш вопрос или команда: ")
        
        if user_input.isupper():
            print("Успокойся")
        elif not user_input:
            print("Как классно, когда ты молчишь. Продолжай в том же духе!")
        else:
            print("Ну и что")

chat_bot()