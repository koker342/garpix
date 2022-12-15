name = input('Введите ваше имя:')
surname = input('Введите вашу фамилию: ')
patronymic = input('Введите ваше отчество: ')
address = input('Введите ваш адрес: ')

print(f"Здравствуйте, {(name[0] + surname[0] + patronymic[0]).upper()}." 
      f" Ваш заказ отправлен по адресу {address.upper()[0] + address[1:]}")