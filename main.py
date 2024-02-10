import customtkinter as ctk
from configparser import ConfigParser

config = ConfigParser()
config.read("ping.ini")

default = "default"
ping = "ping"
p1 = "player1"
p2 = "player2"
p1board = "p1board"
p2board = "p2board"
win_board = "win_board"
win_round = "win_round"

config.set(default, p1 ,"0")
config.set(default, p2 ,"0")
config.set(default, p1board ,"0")
config.set(default, p2board ,"0")
config.set(default, win_board ,"0")
config.set(default, win_round ,"0")
with open("ping.ini", "w") as f:
    config.write(f)

num_board = ctk.CTkInputDialog(text="How many boards do you want to play?", title="Board Number")
board_num = num_board.get_input()
if board_num.isnumeric() == True:
    config.set(default, win_board, str(board_num))
    with open("ping.ini", "w") as f:
        config.write(f)
else:
    pass

num_round = ctk.CTkInputDialog(text="How many rounds do you want to go?", title="Round Number")
round_num = num_round.get_input()
if round_num.isnumeric() == True:
    config.set(default, win_round, str(round_num))
    with open("ping.ini", "w") as f:
        config.write(f)
else:
    pass

root = ctk.CTk()
root.geometry("400x200")

boardframe1 = ctk.CTkFrame(root)
board1 = ctk.CTkLabel(boardframe1, text="Player 1's Board:")
board1.grid(row=0, column=0)
num_board1 = config.get(default, p1board)
board1_num = ctk.CTkLabel(boardframe1, text=num_board1)
board1_num.grid(row=0, column=1)
boardframe2 = ctk.CTkFrame(root)
board2 = ctk.CTkLabel(boardframe2, text="Player 2's Board:")
board2.grid(row=0, column=3)
num_board2 = config.get(default, p2board)
board2_num = ctk.CTkLabel(boardframe2, text=num_board2)
board2_num.grid(row=0, column=4)

boardframe1.grid(row=0, column=0)
boardframe2.grid(row=0, column=1)

frame1 = ctk.CTkFrame(root)
frame1.grid(column=0, row=1)
frame2 = ctk.CTkFrame(root)
frame2.grid(column=1, row=1)

root.mainloop()