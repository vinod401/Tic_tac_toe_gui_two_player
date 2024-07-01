from tkinter import *
from tkinter import messagebox

BG_GREEN = "#6BC395"
GREEN = "#547F55"
SCORE_FONT = ("Bahnschrift", 40)
PLAYER_O_COLOR = "#BEE2CF"
PLAYER_X_COLOR = "#414042"

# to track the turn of the players
turn = 0


def reset_all():
    """this functions reset all the buttons and tracking variables to its default values"""
    button_one.config(image=blank_image, state="normal")
    button_two.config(image=blank_image, state="normal")
    button_three.config(image=blank_image, state="normal")
    button_four.config(image=blank_image, state="normal")
    button_five.config(image=blank_image, state="normal")
    button_six.config(image=blank_image, state="normal")
    button_seven.config(image=blank_image, state="normal")
    button_eight.config(image=blank_image, state="normal")
    button_nine.config(image=blank_image, state="normal")
    result.config(image=o_turn)

    global player_x_rows, player_x_columns, player_x_diagonal_one, \
        player_x_diagonal_two, player_o_rows, player_o_columns, player_o_diagonal_one, player_o_diagonal_two, turn

    # clearing all rows and columns used and resign the diagonal index of the players
    player_x_rows.clear()
    player_x_columns.clear()
    player_x_diagonal_one = [(0, 0), (1, 1), (2, 2)]
    player_x_diagonal_two = [(2, 0), (1, 1), (0, 2)]

    player_o_rows.clear()
    player_o_columns.clear()
    player_o_diagonal_one = [(0, 0), (1, 1), (2, 2)]
    player_o_diagonal_two = [(2, 0), (1, 1), (0, 2)]
    turn = 0


# updates the score and if the user choose to continue the game call the reset function
def update_score():
    """Update the score of players """
    global x_score, o_score

    player_x_score.config(text=x_score)
    player_o_score.config(text=o_score)

    if messagebox.askyesno(message="Do you want to continue game"):
        reset_all()
    else:
        windows.quit()


def check_win():
    """checks whether any player have won or the number of turns is over"""
    global x_score, o_score

    # checking whether the player x won in any of the diagonal
    if len(player_x_diagonal_one) == 0 or len(player_x_diagonal_two) == 0:
        # update the result label
        result.config(image=x_win_image)
        # updating the score of player x
        x_score += 1
        return True

    else:
        # checking whether the player x won in any of the rows and columns
        for i in range(0, 3):

            if player_x_rows.count(i) == 3 or player_x_columns.count(i) == 3:
                result.config(image=x_win_image)
                x_score += 1

                return True

    # checking whether the player o won in any of the diagonal
    if len(player_o_diagonal_one) == 0 or len(player_o_diagonal_two) == 0:
        # update the result label
        result.config(image=o_win_image)
        # updating the score of player o
        o_score += 1

        return True

    else:
        # checking whether the player o won in any of the rows and columns
        for i in range(0, 3):
            if player_o_rows.count(i) == 3 or player_o_columns.count(i) == 3:
                # update the result label
                result.config(image=o_win_image)
                # updating the score of player o
                o_score += 1

                return True

        if turn == 8:
            result.config(image=draw_image)
            return True


def put_char(row, column, button):
    """puts the character in the box where the player clicked according to the turn"""

    global turn

    if turn % 2 == 0:

        # when the turn is divisible by 2 it means that the o player already used his turn and now its x turn
        result.config(image=x_turn)

        # player o
        button.config(image=o_image, state='disabled')
        player_o_rows.append(row)
        player_o_columns.append(column)
        if (row, column) in player_o_diagonal_one:
            player_o_diagonal_one.remove((row, column))
        if (row, column) in player_o_diagonal_two:
            player_o_diagonal_two.remove((row, column))
    else:
        # when the turn is not divisible by 2 it means that the x player already used his turn and now its o turn
        result.config(image=o_turn)
        # player x
        button.config(image=x_image, state='disabled')
        player_x_rows.append(row)
        player_x_columns.append(column)
        if (row, column) in player_x_diagonal_one:
            player_x_diagonal_one.remove((row, column))
        if (row, column) in player_x_diagonal_two:
            player_x_diagonal_two.remove((row, column))

    if check_win():
        update_score()

    else:
        turn += 1


windows = Tk()
windows.title("Tic-Tac-Toe")
windows.minsize(width=620, height=560)
windows.maxsize(width=620, height=560)


# images variable
bg_image = PhotoImage(file="./ui_components/bg-01.png")
x_image = PhotoImage(file="./ui_components/x_img.png")
x_win_image = PhotoImage(file="./ui_components/x_win.png")
o_image = PhotoImage(file="./ui_components/o_img.png")
o_win_image = PhotoImage(file="./ui_components/o_win.png")
o_turn = PhotoImage(file="./ui_components/o_turn.png")
x_turn = PhotoImage(file="./ui_components/x_turn.png")
draw_image = PhotoImage(file="./ui_components/draw.png")
blank_image = PhotoImage(file="./ui_components/blank_button.png")
icon = PhotoImage(file="./ui_components/icon.png")

windows.iconphoto(False, icon)

# the rows and columns are considered a matrix
# when a player clicked on the first box in the first row the index is 0,0 row number is 0 and column number is 0
# this is stored and tracked for each player
#  also the diagonal if the player used any of the diagonal box the index will be deleted from their diagonal list

# checking winning if there is no elements in any of the diagonal list the player have won
# if any index in row or column have 3 same number (example player_x_rows = [0 , 0 , 0 , 1] )
# it indicates the user have won

player_x_rows = []
player_x_columns = []
player_x_diagonal_one = [(0, 0), (1, 1), (2, 2)]
player_x_diagonal_two = [(2, 0), (1, 1), (0, 2)]
x_score = 0

player_o_rows = []
player_o_columns = []
player_o_diagonal_one = [(0, 0), (1, 1), (2, 2)]
player_o_diagonal_two = [(2, 0), (1, 1), (0, 2)]
o_score = 0

canvas = Canvas(width=620, height=560, highlightthickness=0)
the_bg_image = canvas.create_image(310, 280, image=bg_image)
canvas.place(x=0, y=0)

button_one = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                    command=lambda: put_char(row=0, column=0, button=button_one))
button_one.place(x=135, y=50)

button_two = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                    command=lambda: put_char(row=0, column=1, button=button_two))
button_two.place(x=260, y=50)

button_three = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                      command=lambda: put_char(row=0, column=2, button=button_three))
button_three.place(x=385, y=50)

button_four = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                     command=lambda: put_char(row=1, column=0, button=button_four))
button_four.place(x=135, y=168)

button_five = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                     command=lambda: put_char(row=1, column=1, button=button_five))
button_five.place(x=260, y=168)

button_six = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                    command=lambda: put_char(row=1, column=2, button=button_six))
button_six.place(x=385, y=168)

button_seven = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                      command=lambda: put_char(row=2, column=0, button=button_seven))
button_seven.place(x=135, y=286)

button_eight = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                      command=lambda: put_char(row=2, column=1, button=button_eight))
button_eight.place(x=260, y=286)

button_nine = Button(image=blank_image, borderwidth=0, highlightbackground=BG_GREEN, background=BG_GREEN,
                     command=lambda: put_char(row=2, column=2, button=button_nine))
button_nine.place(x=385, y=286)

player_x_score = Label(text="00", foreground=PLAYER_X_COLOR, font=SCORE_FONT, background=GREEN)
player_x_score.place(x=80, y=460)

player_o_score = Label(text="00", foreground=PLAYER_O_COLOR, font=SCORE_FONT, background=GREEN)
player_o_score.place(x=480, y=460)

result = Label(image=o_turn, background=GREEN)
result.place(x=182, y=448)

windows.mainloop()
