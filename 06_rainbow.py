# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)



# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

def bubble(point, step):
    radius = 450
    for i in range(len(rainbow_colors)):
        radius += 15
        sd.circle(center_position=point, radius=radius, color=rainbow_colors[i], width=15)

for _ in range(7):
    point = sd.get_point(600, 0)
    step = 5
    bubble(point=point, step=step)

sd.pause()
