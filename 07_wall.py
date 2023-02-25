# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (600, 600)
sd.background_color = [164, 43, 7]
y2 = 0
number = 0  # Переменная для подсчёта циклов
for y1 in range(0, 600, 50):  # Цикл для постройки кирпичей в высоту
    y2 += 50
    number += 1
    if number % 2 == 0:  # Условие. Если цикл нечётный, то сдвиг кирпичей. Если чётный - оставить на прежнем месте
        x2 = 0
        range_x1 = range(0, 600, 100)
    else:
        x2 = 50
        range_x1 = range(-50, 550, 100)
    for x1 in range_x1:  # Кладём кирпичи в ширину
        x2 += 100
        sd.rectangle(left_bottom=sd.get_point(x1, y1), right_top=sd.get_point(x2, y2), color=sd.COLOR_ORANGE, width=2)
sd.pause()
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for



sd.pause()
