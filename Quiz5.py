d = {"What is the best kind of beer?":'Belgium beer', "What is the worst of beer?":'Indian beer'}
while True:
    ask_user = input(': ')
    if ask_user == "What is the best kind of beer?":
        print('Belgium beer')
    elif ask_user == "What is the worst of beer?":
        print('Indian beer')
        break
    else:
        print('Ask again')




# Создайте словарь типа "вопрос": "ответ", например:
# {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
#* Напишите функцию ask_user() которая с помощью функции input()
 # просит пользователя ввести вопрос, а затем, если вопрос есть
 # в словаре, программа давала ему соотвествующий ответ. Например:
 #   Пользователь: Что делаешь?
  #  Программа: Программирую