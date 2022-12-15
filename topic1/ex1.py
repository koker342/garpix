name = input('')
surname = input('')
patronymic = input('')
address = input('')

print(f"Здравствуйте, {(name[0] + surname[0] + patronymic[0]).upper()}." 
      f" Ваш заказ отправлен по адресу {address.upper()[0] + address[1:]}")