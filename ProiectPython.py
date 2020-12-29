#!/usr/bin/python
import tkinter as tk
import random

nr_of_pieces = 126
buttons1 = []
exists1 = []
buttons2 = []
exists2 = []
buttons3 = []
exists3 = []
colors = [["red", 16], ["yellow", 16], ["blue", 16], ["green", 16], ["orange", 16], ["brown", 16], ["purple", 16],
          ["pink", 14]]
positions = [0, 1, 2, 3, 4, 5, 6, 7]

nr_of_clicks = 0
prec_button_color = "black"
prec_button_x = 0
prec_button_y = 0
prec_button_h = 0
def comand_for_button(actual_button_color, actual_button_x, actual_button_y, actual_button_h):
    global nr_of_clicks, prec_button_color, prec_button_h, prec_button_h, prec_button_x, prec_button_y, nr_of_pieces
    if nr_of_clicks == 0:
        nr_of_clicks = nr_of_clicks + 1
        prec_button_color = actual_button_color
        prec_button_x = actual_button_x
        prec_button_y = actual_button_y
        prec_button_h = actual_button_h
        if actual_button_h == 1:
            buttons1[actual_button_x][actual_button_y].config(bd=10)
        if actual_button_h == 2:
            buttons2[actual_button_x][actual_button_y].config(bd=10)
        if actual_button_h == 3:
            buttons3[actual_button_x][actual_button_y].config(bd=10)
    elif nr_of_clicks == 1:
        if actual_button_color != prec_button_color:
            if prec_button_h == 1:
                buttons1[prec_button_x][prec_button_y].config(bd=2)
            if prec_button_h == 2:
                buttons2[prec_button_x][prec_button_y].config(bd=2)
            if prec_button_h == 3:
                buttons3[prec_button_x][prec_button_y].config(bd=2)
            prec_button_color = actual_button_color
            prec_button_x = actual_button_x
            prec_button_y = actual_button_y
            prec_button_h = actual_button_h
            if actual_button_h == 1:
                buttons1[actual_button_x][actual_button_y].config(bd=10)
            if actual_button_h == 2:
                buttons2[actual_button_x][actual_button_y].config(bd=10)
            if actual_button_h == 3:
                buttons3[actual_button_x][actual_button_y].config(bd=10)
        else:
            nr_of_clicks = 0
            if prec_button_h == 1:
                buttons1[prec_button_x][prec_button_y].place_forget()
            if prec_button_h == 2:
                buttons2[prec_button_x][prec_button_y].place_forget()
            if prec_button_h == 3:
                buttons3[prec_button_x][prec_button_y].place_forget()
            if actual_button_h == 1:
                buttons1[actual_button_x][actual_button_y].place_forget()
            if actual_button_h == 2:
                buttons2[actual_button_x][actual_button_y].place_forget()
            if actual_button_h == 3:
                buttons3[actual_button_x][actual_button_y].place_forget()
            nr_of_pieces = nr_of_pieces - 2

def create_map():
    button_height = 5
    button_width = 10
    top.geometry("760x790")

    # nivelul 1
    pozx = 0
    pozy = 0

    for i in range(0, 9):
        exists = []
        buttonsx = []
        for j in range(0, 9):
            choice = random.choice(positions)
            while colors[choice][1] == 0:
                choice = random.choice(positions)
            button = tk.Button(top, fg="white", state="disabled", bg=colors[choice][0], height=button_height,
                               width=button_width,
                               command=lambda button_color=colors[choice][0], button_x=i, button_y=j, button_h=1:
                               comand_for_button(button_color, button_x, button_y, button_h))
            colors[choice][1] = colors[choice][1] - 1
            exists.append(1)
            buttonsx.append(button)
            buttonsx[-1].place(x=pozx, y=pozy)
            pozx = pozx + 80
        exists1.append(exists1)
        buttons1.append(buttonsx)
        pozy = pozy + 85
        pozx = 0
    buttons1[0][0].config(state="normal")
    buttons1[0][8].config(state="normal")
    buttons1[8][0].config(state="normal")
    buttons1[8][8].config(state="normal")

    # nivelul 2

    pozx = 120
    pozy = 127.5

    for i in range(0, 6):
        buttonsx = []
        exists = []
        for j in range(0, 6):
            choice = random.choice(positions)
            while colors[choice][1] == 0:
                choice = random.choice(positions)
            button = tk.Button(top, fg="white", state="disabled", bg=colors[choice][0], height=button_height,
                               width=button_width,
                               command=lambda button_color=colors[choice][0], button_x=i, button_y=j, button_h=2:
                               comand_for_button(button_color, button_x, button_y, button_h))
            colors[choice][1] = colors[choice][1] - 1
            buttonsx.append(button)
            exists.append(1)
            buttonsx[-1].place(x=pozx, y=pozy)
            pozx = pozx + 80
        exists2.append(exists)
        buttons2.append(buttonsx)
        pozy = pozy + 85
        pozx = 120
    buttons2[0][0].config(state="normal")
    buttons2[0][5].config(state="normal")
    buttons2[5][0].config(state="normal")
    buttons2[5][5].config(state="normal")

    # nivelul 3

    pozx = 240
    pozy = 255

    for i in range(0, 3):
        buttonsx = []
        exists = []
        for j in range(0, 3):
            choice = random.choice(positions)
            while colors[choice][1] == 0:
                choice = random.choice(positions)
            button = tk.Button(top, state="disabled", fg="white", bg=colors[choice][0], height=button_height,
                               width=button_width,
                               command=lambda button_color=colors[choice][0], button_x=i, button_y=j, button_h=3:
                               comand_for_button(button_color, button_x, button_y, button_h))
            colors[choice][1] = colors[choice][1] - 1
            exists.append(1)
            buttonsx.append(button)
            buttonsx[-1].place(x=pozx, y=pozy)
            pozx = pozx + 80
        exists3.append(exists)
        buttons3.append(buttonsx)
        pozy = pozy + 85
        pozx = 240
    buttons3[0][0].config(state="normal")
    buttons3[0][2].config(state="normal")
    buttons3[2][0].config(state="normal")
    buttons3[2][2].config(state="normal")

top = tk.Tk()

create_map()

top.mainloop()
