# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей



# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


# Нарисовать 10 пузырьков в ряд



# Нарисовать три ряда по 10 пузырьков


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


for _ in range(200):
    point = sd.random_point()
    step = random.randint(2, 10)
    bubble(point=point, step=step)



sd.pause()


