from turtle import *
from random import *
from math import *


def building(a, b, distance):
    speed(1)
    setheading(0)
    fillcolor('#0000cd')
    begin_fill()
    for _ in range(4):
        forward(a)
        left(90)
        a, b = b, a
    end_fill()

    penup()
    goto(pos()[0] + distance, pos()[1] + distance)
    pendown()

def window(window_size, distance):
    setheading(0)
    fillcolor(choice(['#ffff52', '#00008a']))

    begin_fill()
    for _ in range(4):
        forward(window_size)
        left(90)
    end_fill()
    left(90)

    Screen().update()

    penup()
    forward(window_size + distance)
    pendown()

def windows(window_size, distance, r_x, r_y):
    speed(1)
    start_y = pos()[1]

    for i in range(r_x):
        for _ in range(r_y):
            speed(1)
            Screen().bgcolor('#00005c')
            window(window_size, distance)
            Screen().update()

        if i != r_x - 1:
            penup()
            goto(pos()[0] + window_size + distance, start_y)
            pendown()
        else:
            penup()
            goto(pos()[0] + window_size + distance, start_y - distance)
            pendown()

def star():
    # поворачиваем
    left(randint(1, 360))

    # перемещаем
    x = randrange(-1600, 1601)
    y = randrange(-800, 801)
    penup()
    goto(x, y)
    pendown()

    # рисуем и закрашиваем
    side, color = randint(1, 30), 'yellow'
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for _ in range(5):
        forward(side)
        right(144)
    end_fill()

def stars():
    for _ in range(999):
        # устанавливаем задержку обновления экрана черепахи на 0 и отключает анимацию
        Screen().tracer(0, 0)
        star()
        Screen().update()

def night_city():
    hideturtle()
    Screen().bgcolor('#00005c')

    window_size = 20
    distance = window_size * 2 / 3

    stars()
    penup()
    goto(-800, -400)
    pendown()
    pencolor('black')

    sum = 0

    while sum < 1600:
        r_x, r_y = randint(2, 6), randint(2, 12)
        x = r_x * (window_size + distance) + distance
        y = r_y * (window_size + distance) + distance
        sum += x
        pencolor('black')
        building(x, y, distance)
        windows(window_size, distance, r_x, r_y)


    done()

night_city()
