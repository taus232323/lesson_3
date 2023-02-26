# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

import simple_draw as sd

sd.resolution = (1200, 600)


def smile(x, y, color): #Функция рисования круга
    start_point = sd.get_point(x, y) #Центр наших смайлов. нужен, чтобы добавить элементы в лицо смайла
    sd.circle(start_point, 50, color, 2) #Рисуем "тело" смайла
    point_list = [sd.Point(x - 25, y - 10), sd.Point(x - 10, y - 20), sd.Point(x - 10, y - 20), sd.Point(x + 10, y - 20),
                  sd.Point(x + 10, y - 20), sd.Point(x + 25, y - 10)] #Задаём координаты улыбки
    sd.lines(point_list, color, False, 2) #Рисуем улыбку с заданными параметрами
    sd.circle(sd.get_point(x - 15, y + 15), 5, color, 2)
    sd.circle(sd.get_point(x + 15, y + 15), 5, color, 2) #Один и другой глаз


for i in range(100): #Вызываем переменную рисования 10 раз
    point = sd.random_point() #В произвольном месте
    x = point.x
    y = point.y # Координаты нужны по заданию. Их можно было избежать
    color = sd.COLOR_YELLOW
    smile(x, y, color)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

sd.pause()
