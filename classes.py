from configparser import ConfigParser
import keyboard
import pygame
from pygame.locals import *
config = ConfigParser()
config.read("test.ini")
default = "default"
p1set = config.get(default, "p1set")
p2set = config.get(default, "p2set")
win_match = config.get(default, "win_match")
win_set = config.get(default, "win_set")
class player(object):
    def __init__(self, Player, set_x, center) -> None:
        self.player = Player
        self.sx = set_x
        self.center = center

    def win_set(self):
        val = config.get(default, f"{self.player}set")
        newval = int(val)+1
        config.set(default, f"{self.player}set", str(newval))
        with open("test.ini","w") as f:
            config.write(f)
    
    def win_point(self):
        val = config.get(default, self.player)
        newval = int(val)+1
        config.set(default, self.player, str(newval))
        with open("test.ini", "w") as f:
            config.write(f)

    def clear_all(self):
        config.set(default, self.player, "0")
        config.set(default, f"{self.player}set", "0")
        config.set(default, "tie", "false")
        with open("ping.ini", "w") as f:
            config.write(f)

    def clear_match(self):
        config.set(default, self.player,"0")
        with open("ping.ini", "w") as f:
            config.write(f)
    
    def point_update(self):
        playerScoreNum = font.render(config.get(default, f"{self.player}set"), 1, (0,0,0))
        win.blit(playerScoreNum,(self.sx, 16.5))
        playerSetNum = point_font.render(config.get(default, self.player), 1, (0,0,0))
        win.blit(playerSetNum,(self.center-playerSetNum.get_width()/2,109))
        pygame.display.update()

def check_set_tie():
    if config.get(default, "p1") == config.get(default, "p2") == "10":
        print("You now need to win by two")
        config.set(default, "tie", "true")
        with open("ping.ini","w") as f:
            config.write(f)       
    else:
        pass

def check_set_win():
    if config.get(default, "tie") == "true":
        if config.get(default, "p1") == f"{int(config.get(default, 'p2'))+2}":
            print("player 1 won this set")
            p1.win_set()
            p1.clear_match()
            p2.clear_match()

        elif config.get(default, "p2") == f"{int(config.get(default, 'p1'))+2}":
            print("player 2 won this set")
            p2.win_set()
            p1.clear_match()
            p2.clear_match()
    else:
        if config.get(default, "p1") == config.get(default, "win_set"):
            print("player 1 won this set")
            p1.win_set()
            p1.clear_match()
            p2.clear_match()
        elif config.get(default, "p2") == config.get(default, "win_set"):
            print("Player 2 won this set")
            p2.win_set()
            p1.clear_match()
            p2.clear_match()
        else:
            pass

def check_match_win():
    if p1set == win_match:
        print("Player 1 has won the match")
        win.fill([255,255,255])
        p1_win = point_font.render("Player 1 Won!!", 1, (0,0,0))
        win.blit(p1_win, (200-p1_win.get_width()/2, 100-p1_win.get_height()/2))
        pygame.display.update()
        pygame.time.wait(5000)
        p1.clear_all()
        p2.clear_all()

    elif p2set == win_match:
        print("Player 2 has won the match")
        win.fill([255,255,255])
        p2_win = point_font.render("Player 2 Won!!", 1, (0,0,0))
        win.blit(p2_win, (200-p2_win.get_width()/2, 100-p2_win.get_height()/2))
        pygame.display.update()
        pygame.time.wait(5000)
        p1.clear_all()
        p2.clear_all()

    else:
        pass

def playerOne():
    p1.win_point()
    check_set_tie()
    check_set_win()

def playerTwo():
    p2.win_point()
    check_set_tie()
    check_set_win()

p1 = player(Player='p1', set_x=151, center=100)
p2 = player(Player='p2', set_x=351, center=300)
p1.clear_all()
p2.clear_all()
pygame.init()
win = pygame.display.set_mode((400,200))
pygame.display.set_caption("Table Tennis Scoring Bot") 
point_font = pygame.font.SysFont('timesnewroman', 30, True)
set_font = pygame.font.SysFont('timesnewroman', 20, True)
font = pygame.font.SysFont('timesnewroman', 15, True)

def redraw_window():
    pygame.draw.rect(win, (255,255,255), (0, 0, 400, 50))
    pygame.draw.rect(win, (255,255,255), (0, 52, 199, 148))
    pygame.draw.rect(win, (255,255,255), (201, 52, 199, 148))
    playerOneScore = font.render('Player 1 Score: ', 1, (0,0,0))
    playerTwoScore = font.render('Player 2 Score: ', 1, (0,0,0))
    playerOneSet = set_font.render('Set:', 1, (0,0,0))
    playerTwoSet = set_font.render('Set:', 1, (0,0,0))
    win.blit(playerOneScore,(44,16.5))
    win.blit(playerTwoScore,(244,16.5))    
    win.blit(playerOneSet,(83,65))
    win.blit(playerTwoSet,(283,65))
    p1.point_update()
    p2.point_update()
    pygame.display.update()

run=True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key==K_LEFT:
                playerOne()
            elif event.key==K_RIGHT:
                playerTwo()
    win.fill([0,0,0])
    redraw_window()
pygame.quit