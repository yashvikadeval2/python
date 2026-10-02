from tkinter import *
import random

# Create window
root=Tk()
root.title("Number Puzzle - 2 Players")
root.geometry("400x500")

# Variables
player=1
score1=0
score2=0
moves=0

# Create puzzle numbers
numbers=list(range(1, 9))+[""]
random.shuffle(numbers)

buttons=[]

def check_win():
    global player, score1, score2, moves

    current = [b["text"] for b in buttons]

    if current == ["1", "2", "3", "4", "5", "6", "7", "8", ""]:
        if player == 1:
            score1 += 1
        else:
            score2 += 1

        score_label.config(
            text="Player 1: " + str(score1) +
                 "     Player 2: " + str(score2)
        )

        result_label.config(text="Player " + str(player) + " WINS!")

        new_game_button.config(state=NORMAL)

def move(pos):
    global moves, player

    blank = buttons.index(next(
        b for b in buttons if b["text"] == ""
    ))

    # Check if selected box is next to blank box
    if abs(pos - blank) == 1 or abs(pos - blank) == 3:

        buttons[blank]["text"], buttons[pos]["text"] = \
            buttons[pos]["text"], buttons[blank]["text"]

        moves += 1

        # Change player after every valid move
        if player == 1:
            player = 2
        else:
            player = 1

        turn_label.config(text="Player " + str(player) + "'s Turn")

        check_win()

def new_game():
    global numbers, player, moves

    numbers = list(range(1, 9)) + [""]
    random.shuffle(numbers)

    player = 1
    moves = 0

    result_label.config(text="")
    turn_label.config(text="Player 1's Turn")

    new_game_button.config(state=DISABLED)

    for i in range(9):
        buttons[i]["text"] = str(numbers[i])


# Title
title = Label(
    root,
    text="NUMBER PUZZLE",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Player turn
turn_label = Label(
    root,
    text="Player 1's Turn",
    font=("Arial", 14)
)
turn_label.pack()

# Score
score_label = Label(
    root,
    text="Player 1: 0     Player 2: 0",
    font=("Arial", 12)
)
score_label.pack(pady=10)

# Puzzle frame
frame = Frame(root)
frame.pack()

# Create 9 buttons
for i in range(9):
    button = Button(
        frame,
        text=str(numbers[i]),
        font=("Arial", 20, "bold"),
        width=5,
        height=2,
        command=lambda x=i: move(x)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    buttons.append(button)

# Result
result_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold")
)
result_label.pack(pady=10)

# New game button
new_game_button = Button(
    root,
    text="New Game",
    font=("Arial", 12),
    command=new_game
)
new_game_button.pack(pady=10)

root.mainloop()