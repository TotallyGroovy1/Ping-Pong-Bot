import pygame
from pygame.locals import *
from configparser import ConfigParser
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
def matchpoint():
    if config.get(default, tie) == "true":
        if config.get(default, p1) == int(config.get(default, p2))+1:
            match_point.play()
            pass
        elif config.get(default, p2) == int(config.get(default, p1))+1:
            match_point.play()
            
    elif config.get(default, tie) == "false":
        if config.get(default, p1) == "10" or config.get(default, p2) == "10":
            match_point.play()
            pass
    

def p1_win_set():
    val = config.get(default,p1set)
    newval = int(val)+1
    config.set(default, p1set, str(newval))
    with open("ping.ini","w") as f:
        config.write(f)
    playerOneScoreNum = font.render(config.get(default, p1set), 1, (0,0,0))
    win.blit(playerOneScoreNum,(151, 16.5))
    pygame.display.update()
    clear_match()
    check_match_win()

def p2_win_set():
    val = config.get(default, p2set)
    newval = int(val)+1
    config.set(default, p2set, str(newval))
    with open("ping.ini","w") as f:
        config.write(f)
    playerTwoScoreNum = font.render(config.get(default, p2set), 1, (0,0,0))
    win.blit(playerTwoScoreNum,(351, 16.5))
    pygame.display.update()
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
        overtime.play()
    else:
        pass

def p1_win_point():
    val = config.get(default, p1)
    newval = int(val) + 1
    config.set(default, p1, str(newval))
    with open("ping.ini", "w") as f:
        config.write(f)
    playerOneSetNum = point_font.render(config.get(default, p1), 1, (0,0,0))
    win.blit(playerOneSetNum,(100-playerOneSetNum.get_width()/2,109))
    pygame.display.update()
    matchpoint()
    check_set_tie()
    check_set_win()

def p2_win_point():
    val = config.get(default, p2)
    newval = int(val)+1
    config.set(default, p2, str(newval))
    with open("ping.ini", "w") as f:
        config.write(f)
    playerTwoSetNum = point_font.render(config.get(default, p2), 1, (0,0,0))
    win.blit(playerTwoSetNum,(300-playerTwoSetNum.get_width()/2,109))
    pygame.display.update()
    matchpoint() 
    check_set_tie()
    check_set_win()

config.set(default, p1, "0")
config.set(default, p2, "0")
config.set(default, p1set, "0")
config.set(default, p2set, "0")
config.set(default, tie, "false")
with open("ping.ini", "w") as f:
    config.write(f)
    
pygame.init()
win = pygame.display.set_mode((400,200))
pygame.display.set_caption("Table Tennis Scoring Bot")

def redraw_window():
    pygame.draw.rect(win, (255,255,255), (0, 0, 400, 50))
    pygame.draw.rect(win, (255,255,255), (0, 52, 199, 148))
    pygame.draw.rect(win, (255,255,255), (201, 52, 199, 148))
    playerOneScore = font.render('Player 1 Score: ', 1, (0,0,0))
    playerTwoScore = font.render('Player 2 Score: ', 1, (0,0,0))
    playerOneSet = set_font.render('Set:', 1, (0,0,0))
    playerTwoSet = set_font.render('Set:', 1, (0,0,0))
    playerOneScoreNum = font.render(config.get(default, p1set), 1, (0,0,0))
    playerTwoScoreNum = font.render(config.get(default, p2set), 1, (0,0,0))
    playerOneSetNum = point_font.render(config.get(default, p1), 1, (0,0,0))
    playerTwoSetNum = point_font.render(config.get(default, p2), 1, (0,0,0))
    win.blit(playerOneScoreNum,(151, 16.5))
    win.blit(playerTwoScoreNum,(351, 16.5))
    win.blit(playerOneScore,(44,16.5))
    win.blit(playerTwoScore,(244,16.5))    
    win.blit(playerOneSet,(83,65))
    win.blit(playerTwoSet,(283,65))
    win.blit(playerOneSetNum,(100-playerOneSetNum.get_width()/2,109))
    win.blit(playerTwoSetNum,(300-playerTwoSetNum.get_width()/2,109))
    pygame.display.update()

match_point = pygame.mixer.Sound('audio\\matchpoint.mp3')
endgame = pygame.mixer.Sound('audio\\endgame.mp3')
overtime = pygame.mixer.Sound('audio\\overtime.mp3')
point_font = pygame.font.SysFont('timesnewroman', 30, True)
set_font = pygame.font.SysFont('timesnewroman', 20, True)
font = pygame.font.SysFont('timesnewroman', 15, True)
run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key==K_LEFT:
                p1_win_point()
            elif event.key==K_RIGHT:
                p2_win_point()
    win.fill([0,0,0])
    redraw_window()

pygame.quit()            