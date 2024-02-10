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



root = ctk.CTk()
root.geometry("400x200")

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

boardframe1 = ctk.CTkFrame(root,width=200)
board1 = ctk.CTkLabel(boardframe1, text="Player 1's Board:")
board1.grid(row=0, column=0, sticky="nsew")
num_board1 = config.get(default, p1board)
board1_num = ctk.CTkLabel(boardframe1, text=num_board1)
board1_num.grid(row=0, column=1, sticky="nsew")

boardframe2 = ctk.CTkFrame(root, width=200)
board2 = ctk.CTkLabel(boardframe2, text="Player 2's Board:")
board2.grid(row=0, column=3, sticky="nsew")
num_board2 = config.get(default, p2board)
board2_num = ctk.CTkLabel(boardframe2, text=num_board2)
board2_num.grid(row=0, column=4, sticky="nsew")
boardframe1.grid(row=0, column=0, sticky="nsew")
boardframe2.grid(row=0, column=1, sticky="nsew")


frame1 = ctk.CTkFrame(root, width=200)
frame1.grid(column=0, row=1, sticky="nsew")

p1round = ctk.CTkLabel(frame1, text=config.get(default, p1))

p1round.grid(sticky="nsew")


frame2 = ctk.CTkFrame(root, width=200)

p2round = ctk.CTkLabel(frame2, text=config.get(default, p2))
p2round.grid(sticky="nsew")

frame2.grid(column=1, row=1, sticky="nsew")
root.columnconfigure(tuple(range(60)), weight=1)
root.rowconfigure(tuple(range(30)), weight=1)
root.mainloop()