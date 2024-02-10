from configparser import ConfigParser

config = ConfigParser()
config.read("ping.ini")
default = "default"
ping = "ping"
p1 = "player1"
p2 = "player2"
p1match = "p1match"
p2match = "p2match"
win_match = "win_match"
win_round = "win_round"

def clear_round():
    config.set(default, p1,"0")
    config.set(default, p2, "0")
    with open("pong.ini", "w") as f:
        config.write(f)

def p1_wins():
    val = int(config.get(default,p1))
    newval = val+1
    config.set(default, p1, newval)
    with open("pong.ini") as f:
        config.write(f)
def p2_wins():
    val = int(config.get(default,p2))
    newval = val+1
    config.set(default, p2, newval)
    with open("pong.ini") as f:
        config.write(f)

config.set(default, p1 ,"0")
config.set(default, p2 ,"0")
config.set(default, p1match ,"0")
config.set(default, p2match ,"0")
with open("ping.ini", "w") as f:
    config.write(f)

if config.get(default, p1) and config.get(default, p2) == 10:
    print("Must win by 2")
elif config.get(default, p1) >= 10:
    pass
elif config.get(default, p1) == 11:
    print("player 1 won this round, match two begins")
    p1_wins()

elif config.get(default, p2) >= 10:
    pass
elif config.get(default, p2) == 11:
    print("player 2 won this round, match two begins")
    p2_wins()

if config.get(default, p1match) > 3:
    pass
elif config.get(default, p1match) == 3:
    print("p1 has won this match, the next ")


num_of_rnds = input("how many rounds do you want to play?")