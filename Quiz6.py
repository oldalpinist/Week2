while True:
    try:
        user_say = input('How are you?: ')
        if user_say == 'Good':
            break
    except KeyboardInterrupt:
        print('Bye')
    break




#Перепишите функцию hello_user() из задания while1, чтобы она
#  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
#  и завершала работу при помощи оператора break