username = input('Введите Ваше имя: ')  # имя пользователя
print('Здравствуйте,', username)
title1 = input('Введите заголовок заметки 1: ')  # заголовок заметки
print('Заметка1: ', title1)
title2 = input('Введите заголовок заметки 2: ')
print('Заметка2: ', title2)
title3 = input('Введите заголовок заметки 3: ')
print('Заметка3: ', title3)
title = [title1, title2, title3]
content = input('Введите описание заметки: ')  # описание заметки
print('Описание: ', content)
status = input('Статус заметки: ')  # статус заметки
print('Статус: ', status)
created_date = input('Введите дату создания заметки в формате DD.MM.YYYY: ')  # дата создания заметки
print('Дата создания заметки: ', created_date[:6])
issue_date = input('Введите дату истечения заметки в формате DD.MM.YYYY: ')  # дата истечения заметки
print('Дата истечения заметки: ', issue_date[:6])
note = [username, content, status, created_date, issue_date]  # вложенный список
print('Собранная информация о заметке: ', note)
print('Список заголовков: ', title)
my_dict = {'Имя': username, 'Список заголовков': title, 'Описание': content, 'Статус': status,
        'Дата создания': created_date, 'Дата истечения': issue_date}  # вложенный словарь
print('Словарь: ', my_dict)
