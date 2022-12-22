password = '123'
quit_programm = ''
while quit_programm != 'q':
    entered_pass = input()
    if entered_pass == password:
        print('Пароль введен верно')
        quit_programm = 'q'
    elif entered_pass == 'q':
        quit_programm = entered_pass
    else:
        print('Попробуйте еще раз')         