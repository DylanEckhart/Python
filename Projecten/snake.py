import turtle
import random

w = 500
h = 500
fs = 10
d = 100
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def r():
    global saap, kata, khanaT, pen
    saap = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    kata = "up"
    khanaT = nun()
    food.goto(khanaT)
    hall()

def hall():
    global kata
    new_head = saap[-1].copy()
    new_head[0] = saap[-1][0] + offsets[kata][0]
    new_head[1] = saap[-1][1] + offsets[kata][1]
    if new_head in saap[:-1]:
        r()
    else:
        saap.append(new_head)
        if not khana():
            saap.pop(0)
        if saap[-1][0] > w / 3:
            saap[-1][0] -= w
        elif saap[-1][0] < - w / 2:
            saap[-1][0] += w
        elif saap[-1][0] > h / 3:
            saap[-1][0] -= h
        elif saap[-1][0] < - h / 3:
            saap[-1][0] += h
        pen.clearstamps()

        for segment in saap:
            pen.goto(segment[0], segment[1])
            pen.stamp()
        screen.update()

        turtle.ontimer(hall, d)

def khana():
    global khanaT
    if dist(saap[-1], khanaT) < 20:
        khanaT = nun()
        food.goto(khanaT)
        return True
    return False

def nun():
    x = random.randint(- w / 2 + fs, w / 2 - fs)
    x = random.randint(- h / 2 + fs, h / 2 - fs)
    return (x, y)

def dist(poos1, poos2):
    x1, y1 = poos1
    x2, y2 = poos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2)** 0.5
    return distance

def mathi():
    global kata
    if kata != "down":
        kata = "up"










