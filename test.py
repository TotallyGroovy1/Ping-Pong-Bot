from configparser import ConfigParser
import keyboard

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

def clear_match():
    config.set(default, p1,"0")
    config.set(default, p2, "0")
    with open("pong.ini", "w") as f:
        config.write(f)

def check_match_win():
    if config.get(default, p1set) == 3:
        print("Player 1 has won the match")
    elif config.get(default, p2set) == 3:
        print("Player 2 has won the match")
    else:
        pass

def check_set_win():
    if config.get(default, p1) == 11:
        print("player 1 won this set")
        p1_win_set()
    elif config.get(default, p2) == 11:
        print("Player 2 won this set")
        p2_win_set()
    else:
        pass

def check_set_tie():
    if config.get(default, p1) and config.get(default, p2) == 10:
        print("You now need to win by two")
    else:
        pass

def p1_win_set():
    val = int(config.get(default,p1set))
    newval = val+1
    config.set(default, p1set, newval)
    with open("pong.ini") as f:
        config.write(f)
def p2_win_set():
    val = int(config.get(default,p2set))
    newval = val+1
    config.set(default, p2set, newval)
    with open("pong.ini") as f:
        config.write(f)

def p1_win_point():
    val = int(config.get(default, p1))
    newval = val+1
    config.set(default, p1, str(newval))
    with open("pong.ini", "w") as f:
        config.write(f)
    check_set_tie()
    check_set_win()
def p2_win_point():
    val = int(config.get(default, p2))
    newval = val+1
    config.set(default, p2, str(newval))
    with open("pong.ini", "w") as f:
        config.write(f)
    check_set_tie()
    check_set_win()




config.set(default, p1 ,"0")
config.set(default, p2 ,"0")
config.set(default, p1set,"0")
config.set(default, p2set,"0")
with open("ping.ini", "w") as f:
    config.write(f)

def game():
    while config.get(default, p1set) and config.get(default, p2set) != 11:
        check_match_win()
        if keyboard.read_key() == "left":
            print("left")
            p1_win_point()
            continue
        elif keyboard.read_key() == 'right':
            print("right")
            p2_win_point()
            continue


game()