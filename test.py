from configparser import ConfigParser
import keyboard
import customtkinter as ctk
from pynput import keyboard

config = ConfigParser()
config.read("ping.ini")
default = "default"
ping = "ping"
p1 = "player1"
p2 = "player2"
p1set = "p1set"
p2set = "p2set"
win_set = "win_set"
win_match = "win_match"
tie = "tie"

def clear_all():
    print("New Game")
    config.set(default, p1, "0")
    config.set(default, p2, "0")
    config.set(default, p1set, "0")
    config.set(default, p2set, "0")
    config.set(default, tie, "false")
    with open("ping.ini", "w") as f:
        config.write(f)

def clear_match():
    config.set(default, p1,"0")
    config.set(default, p2, "0")
    with open("ping.ini", "w") as f:
        config.write(f)

def check_match_win():
    if config.get(default, p1set) == "3":
        print("Player 1 has won the match")
        clear_all()
    elif config.get(default, p2set) == "3":
        print("Player 2 has won the match")
        clear_all()
    else:
        pass

def p1_win_set():
    val = config.get(default,p1set)
    newval = int(val)+1
    config.set(default, p1set, str(newval))
    with open("ping.ini","w") as f:
        config.write(f)
    clear_match()
    check_match_win()

def p2_win_set():
    val = config.get(default, p2set)
    newval = int(val)+1
    config.set(default, p2set, str(newval))
    with open("ping.ini","w") as f:
        config.write(f)
    clear_match()
    check_match_win()

def check_set_win():
    if config.get(default, tie) == "true":
        if config.get(default, p1) == f"{int(config.get(default, p2))+2}":
            print("player 1 won this set")
            p1_win_set()
        elif config.get(default, p2) == f"{int(config.get(default, p1))+2}":
            print("player 2 won this set")
            p2_win_set()
    else:
        if config.get(default, p1) == "11":
            print("player 1 won this set")
            p1_win_set()
        elif config.get(default, p2) == "11":
            print("Player 2 won this set")
            p2_win_set()
        else:
            pass

def check_set_tie():
    if config.get(default, p1) == config.get(default, p2) == "10":
        print("You now need to win by two")
        config.set(default, tie, "true")
        with open("ping.ini","w") as f:
            config.write(f)
    else:
        pass

def p1_win_point():
    val = config.get(default, p1)
    newval = int(val) + 1
    config.set(default, p1, str(newval))
    with open("ping.ini", "w") as f:
        config.write(f)
    check_set_tie()
    check_set_win()

def p2_win_point():
    val = config.get(default, p2)
    newval = int(val)+1
    config.set(default, p2, str(newval))
    with open("ping.ini", "w") as f:
        config.write(f)
    check_set_tie()
    check_set_win()


config.set(default, p1, "0")
config.set(default, p2, "0")
config.set(default, p1set, "0")
config.set(default, p2set, "0")
config.set(default, tie, "false")
with open("ping.ini", "w") as f:
    config.write(f)
"""     keyboard.add_hotkey('left', p1_win_point)
    keyboard.add_hotkey('right', p2_win_point)
    keyboard.wait() """
def game():
    check_match_win()

    listener = keyboard.GlobalHotKeys({
        '<left>': p1_win_point,
        '<right>': p2_win_point})
    listener.start()
    
    root = ctk.CTk()

    frame1 = ctk.CTkFrame(root)



    frame2 = ctk.CTkFrame(root)



    frame3 = ctk.CTkFrame(root)



    frame1.grid()
    frame2.grid()
    frame3.grid()
    root.mainloop()  
    while True:
        pass  

game()