# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
if month == 1:
    month = 'january'
    print('Вы ввели', month, 'месяц, в нём 31 день')
elif month == 2:
    print('Вы ввели', month, 'месяц, в нём 28 дней')
elif month == 3:
    print('Вы ввели', month, 'месяц, в нём 31 день')
elif month == 4:
    print('Вы ввели', month, 'месяц, в нём 30 дней')
elif month == 5:
    print('Вы ввели', month, 'месяц, в нём 31 день')
elif month == 6:
    print('Вы ввели', month, 'месяц, в нём 30 дней')
elif month == 7:
    print('Вы ввели', month, 'месяц, в нём 31 день')
elif month == 8:
    print('Вы ввели', month, 'месяц, в нём 31 день')
elif month == 9:
    print('Вы ввели', month, 'месяц, в нём 30 дней')
elif month == 10:
    print('Вы ввели', month, 'месяц, в нём 31 день')
elif month == 11:
    print('Вы ввели', month, 'месяц, в нём 30 дней')
elif month == 12:
    print('Вы ввели', month, 'месяц, в нём 31 день')
else:
    print('Введите порядковый номер месяца(цифра от 1 до 12)')
