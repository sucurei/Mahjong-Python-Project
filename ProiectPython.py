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
colors = [["navy", 6], ["cyan", 6], ["khaki", 6], ["gold", 6], ["gray20", 6], ["red", 6], ["purple", 6],
          ["seashell4", 6], ["gray60", 6], ["blue2", 6], ["cyan4", 6], ["SeaGreen1", 6], ["green4", 6],
          ["OliveDrab1", 6], ["yellow2", 6], ["goldenrod2", 6], ["IndianRed1", 6], ["tan4", 6], ["firebrick4", 6],
          ["DeepPink2", 6], ["MediumPurple3", 6]]
positions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def playable():
    """
    Every time a modification was made on the table game, this function will be called to verify if the game is still
    playable or not. The function will check every card of the game, level by level to see if there is a pair that
    could be selected.
    :return: 1 when the game is still playable(there are selectable pairs)
             0 when there are no more pairs to be selected. In this case player lose.
    """
    # nivelul 1
    for i in range(0, 9):
        for j in range(0, 9):
            if exists1[i][j] == 1 and buttons1[i][j]["state"] == "normal":
                # cu nivelul 1
                for x in range(0, 9):
                    for y in range(0, 9):
                        if exists1[x][y] == 1 and buttons1[x][y]["state"] == "normal" and \
                                buttons1[i][j]["bg"] == buttons1[x][y]["bg"] and not(i == x and j == y):
                            return 1
                # cu nivelul 2
                for x in range(0, 6):
                    for y in range(0, 6):
                        if exists2[x][y] == 1 and buttons2[x][y]["state"] == "normal" and \
                                buttons1[i][j]["bg"] == buttons2[x][y]["bg"]:
                            return 1
                # cu nivelul 3
                for x in range(0, 3):
                    for y in range(0, 3):
                        if exists3[x][y] == 1 and buttons3[x][y]["state"] == "normal" and \
                                buttons1[i][j]["bg"] == buttons3[x][y]["bg"]:
                            return 1

    # nivelul 2
    for i in range(0, 6):
        for j in range(0, 6):
            if exists2[i][j] == 1 and buttons2[i][j]["state"] == "normal":
                # cu nivelul 2
                for x in range(0, 6):
                    for y in range(0, 6):
                        if exists2[x][y] == 1 and buttons2[x][y]["state"] == "normal" and \
                                buttons2[i][j]["bg"] == buttons2[x][y]["bg"] and not(i == x and j == y):
                            return 1
                # cu nivelul 3
                for x in range(0, 3):
                    for y in range(0, 3):
                        if exists3[x][y] == 1 and buttons3[x][y]["state"] == "normal" and \
                                buttons2[i][j]["bg"] == buttons3[x][y]["bg"]:
                            return 1

    # nivelul 3
    for i in range(0, 3):
        for j in range(0, 3):
            if exists3[i][j] == 1 and buttons3[i][j]["state"] == "normal":
                # cu nivelul 3
                for x in range(0, 3):
                    for y in range(0, 3):
                        if exists3[x][y] == 1 and buttons3[x][y]["state"] == "normal" and \
                                buttons3[i][j]["bg"] == buttons3[x][y]["bg"] and not(i == x and j == y):
                            return 1
    return 0


def nr_of_neighbours(h, x, y):
    """
    This function will help to find more easily if a piece is or isn't selectable. This function count the number of the
    neighbours up, down, left and right for the piece which is at the level 'h', line 'x' and column 'y'
    :param h: On which level the piece is
    :param x: On which line the piece is
    :param y: On which column the piece is
    :return: cnt which represents the number of neighbours
    """
    cnt = 0
    if h == 1:
        if exists1[x][y-1] == 1:
            cnt = cnt + 1
        if exists1[x][y+1] == 1:
            cnt = cnt + 1
        if exists1[x-1][y] == 1:
            cnt = cnt + 1
        if exists1[x+1][y] == 1:
            cnt = cnt + 1
    elif h == 2:
        if exists2[x][y-1] == 1:
            cnt = cnt + 1
        if exists2[x][y+1] == 1:
            cnt = cnt + 1
        if exists2[x-1][y] == 1:
            cnt = cnt + 1
        if exists2[x+1][y] == 1:
            cnt = cnt + 1
    elif h == 3:
        if exists3[x][y - 1] == 1:
            cnt = cnt + 1
        if exists3[x][y + 1] == 1:
            cnt = cnt + 1
        if exists3[x - 1][y] == 1:
            cnt = cnt + 1
        if exists3[x + 1][y] == 1:
            cnt = cnt + 1
    return cnt


def make_buttons_state_normal():
    """
    This procedure make every button state of the game to be normal.
    :return:none
    """
    for i in range(0, 9):
        for j in range(0, 9):
            buttons1[i][j].config(state="normal")
    for i in range(0, 6):
        for j in range(0, 6):
            buttons2[i][j].config(state="normal")
    for i in range(0, 3):
        for j in range(0, 3):
            buttons3[i][j].config(state="normal")


def update_button_state_by_neighbours():
    """
    This procedure will make every button's state disabled if the piece of the game that meet the button has neighbours
    on both left and right side in the same time.
    :return: none
    """
    # nivelul 1
    for i in range(0, 9):
        for j in range(1, 8):
            if exists1[i][j] == 1:
                if i == 0 or i == 8:
                    if exists1[i][j-1] == 1 and exists1[i][j+1] == 1:
                        buttons1[i][j].config(state="disabled")
                else:
                    if nr_of_neighbours(1, i, j) == 4:
                        buttons1[i][j].config(state="disabled")
                    if nr_of_neighbours(1, i, j) < 4:
                        if exists1[i][j-1] == 1 and exists1[i][j+1] == 1:
                            buttons1[i][j].config(state="disabled")

    # nivelul 2
    for i in range(0, 6):
        for j in range(1, 5):
            if exists2[i][j] == 1:
                if i == 0 or i == 5:
                    if exists2[i][j - 1] == 1 and exists2[i][j + 1] == 1:
                        buttons2[i][j].config(state="disabled")
                else:
                    if nr_of_neighbours(2, i, j) == 4:
                        buttons2[i][j].config(state="disabled")
                    if nr_of_neighbours(2, i, j) < 4:
                        if exists2[i][j - 1] == 1 and exists2[i][j + 1] == 1:
                            buttons2[i][j].config(state="disabled")

    # nivelul 3
    for i in range(0, 3):
        for j in range(1, 2):
            if exists3[i][j] == 1:
                if i == 0 or i == 2:
                    if exists3[i][j - 1] == 1 and exists3[i][j + 1] == 1:
                        buttons3[i][j].config(state="disabled")
                else:
                    if nr_of_neighbours(3, i, j) == 4:
                        buttons3[i][j].config(state="disabled")
                    if nr_of_neighbours(3, i, j) < 4:
                        if exists3[i][j - 1] == 1 and exists3[i][j + 1] == 1:
                            buttons3[i][j].config(state="disabled")


def update_button_state_by_level():
    """
    This procedure will make every button that has another button on them to be disabled.
    :return: none
    """
    # nivelul 3
    to_disable = []
    for i in range(0, 3):
        for j in range(0, 3):
            if exists3[i][j] == 1:
                to_disable.append([i + 1, j + 1])
                to_disable.append([i + 1, j + 2])
                to_disable.append([i + 2, j + 1])
                to_disable.append([i + 2, j + 2])
    for i in to_disable:
        buttons2[i[0]][i[1]].config(state="disabled")

    # nivelul 2
    to_disable = []
    for i in range(0, 6):
        for j in range(0, 6):
            if exists2[i][j] == 1:
                to_disable.append([i + 1, j + 1])
                to_disable.append([i + 1, j + 2])
                to_disable.append([i + 2, j + 1])
                to_disable.append([i + 2, j + 2])
    for i in to_disable:
        buttons1[i[0]][i[1]].config(state="disabled")


def update_button_state():
    """
    This procedure will verify if a button should be disabled or not.
    :return: none
    """
    update_button_state_by_level()
    update_button_state_by_neighbours()


nr_of_clicks = 0
prec_button_color = "black"
prec_button_x = 0
prec_button_y = 0
prec_button_h = 0


def comand_for_button(actual_button_color, actual_button_x, actual_button_y, actual_button_h):
    """
    If there are no buttons selected, this procedure will make the border of the button thicker to be more
    visible, will save it's colour and it's coordinates and will wait for another button to be pressed.
    If there is a pressed button, this procedure will verify if the colours of the actual button and the last button
    pressed is the same or not to see if those buttons can be deleted from the table.
    If two buttons are deleted, this procedure will also verify if the game is still playable, calling the function
    'playable' to see if the game could continue or not; and will verify if the 'nr_of_pieces' variable is 0, in this
    case the player win.
    :param actual_button_color: the pressed button color
    :param actual_button_x: the pressed button line
    :param actual_button_y: the pressed button column
    :param actual_button_h: the pressed button level
    :return: none
    """
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
    elif nr_of_clicks == 1 and not (actual_button_h == prec_button_h and actual_button_x == prec_button_x and
                                    actual_button_y == prec_button_y):
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
                exists1[prec_button_x][prec_button_y] = 0
            if prec_button_h == 2:
                buttons2[prec_button_x][prec_button_y].place_forget()
                exists2[prec_button_x][prec_button_y] = 0
            if prec_button_h == 3:
                buttons3[prec_button_x][prec_button_y].place_forget()
                exists3[prec_button_x][prec_button_y] = 0
            if actual_button_h == 1:
                buttons1[actual_button_x][actual_button_y].place_forget()
                exists1[actual_button_x][actual_button_y] = 0
            if actual_button_h == 2:
                buttons2[actual_button_x][actual_button_y].place_forget()
                exists2[actual_button_x][actual_button_y] = 0
            if actual_button_h == 3:
                buttons3[actual_button_x][actual_button_y].place_forget()
                exists3[actual_button_x][actual_button_y] = 0
            nr_of_pieces = nr_of_pieces - 2
            make_buttons_state_normal()
            update_button_state()
    if nr_of_pieces == 0:
        final = tk.Tk()

        message = tk.Button(final, text="You WON!!!", padx=20, pady=30, state="disabled")
        message.pack()

        final.mainloop()
    elif playable() == 0:
        final = tk.Tk()

        message = tk.Button(final, text="There are no more matches. You LOST!!!", padx=20, pady=30, state="disabled")
        message.pack()

        final.mainloop()


def create_map():
    """
    This procedure will generate the map, and make the game playable.
    :return: none
    """
    button_height = 5
    button_width = 10
    top.geometry("720x790")

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
        exists1.append(exists)
        buttons1.append(buttonsx)
        pozy = pozy + 85
        pozx = 0
    for i in range(0, 9):
        buttons1[i][0].config(state="normal")
        buttons1[i][8].config(state="normal")

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
    for i in range(0, 6):
        buttons2[i][0].config(state="normal")
        buttons2[i][5].config(state="normal")

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
    for i in range(0, 3):
        buttons3[i][0].config(state="normal")
        buttons3[i][2].config(state="normal")


top = tk.Tk()

create_map()

top.mainloop()
