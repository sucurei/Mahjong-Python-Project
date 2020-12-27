#!/usr/bin/python
import Tkinter as tk
import random

buttonHeight = 5
buttonWidth = 10
buttons1 = []
buttons2 = []
buttons3 = []
collors = [["red",16],["yellow",16],["blue",16],["green",16],["orange",16],["brown",16],["purple",16],["pink",14]]
positions = [0,1,2,3,4,5,6,7]

top = tk.Tk()
top.geometry("760x790")

# nivelul 1
X=0
Y=0

for i in range(1,10):
    for j in range(1,10):
        choice = random.choice(positions)
        while collors[choice][1] == 0:
            choice = random.choice(positions)
        button = tk.Button(top,fg="white",bg=collors[choice][0],height = buttonHeight, width = buttonWidth)
        collors[choice][1] = collors[choice][1] - 1 
        buttons1.append(button)
        buttons1[-1].place(x=X,y=Y)
        X=X+80
    Y=Y+85
    X=0

# nivelul 2

X=120
Y=127.5

for i in range(1,7):
    for j in range(1,7):
        choice = random.choice(positions)
        while collors[choice][1] == 0:
            choice = random.choice(positions)
        button = tk.Button(top,fg="white",bg=collors[choice][0],height = buttonHeight, width = buttonWidth)
        collors[choice][1] = collors[choice][1] - 1 
        buttons2.append(button)
        buttons2[-1].place(x=X,y=Y)
        X=X+80
    Y=Y+85
    X=120

# nivelul 3

X=240
Y=255

for i in range(1,4):
    for j in range(1,4):
        choice = random.choice(positions)
        while collors[choice][1] == 0:
            choice = random.choice(positions)
        button = tk.Button(top,fg="white",bg=collors[choice][0],height = buttonHeight, width = buttonWidth)
        collors[choice][1] = collors[choice][1] - 1 
        buttons3.append(button)
        buttons3[-1].place(x=X,y=Y)
        X=X+80
    Y=Y+85
    X=240

top.mainloop()