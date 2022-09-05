from operator import truediv
from turtle import position
import pygame

pygame.init()

#game variables
screen_width = 600
screen_height = 600
line_width = 10

moves = [[0,0,0], [0,0,0], [0,0,0]]  # 0 means nobody picked that spot, 1 means player 1, 2 means player 2
player = 1

#colors
grey = (50, 50, 50)
white = (255, 255, 255)
blue = (50, 100, 200) #player 1
green = (0, 255, 100) #player 2
darkrose = (150, 40, 70)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-Tac-Toe')

def draw_grid():
    background = darkrose
    screen.fill(background)
    line_color = white
    #horizontal lines
    pygame.draw.line(screen, line_color, (0,200), (screen_width, 200), line_width)
    pygame.draw.line(screen, line_color, (0,400), (screen_width, 400), line_width)
    #vertical lines
    pygame.draw.line(screen, line_color, (200, 0), (200, screen_height), line_width)
    pygame.draw.line(screen, line_color, (400, 0), (400, screen_height), line_width)

def draw_x(x, y): # x is player 1
    pygame.draw.line(screen, blue, (x*200 + 50, y*200 + 50), (x*200 + 150, y*200 + 150), line_width)
    pygame.draw.line(screen, blue, (x*200 + 150, y*200 + 50), (x*200 + 50, y*200 + 150), line_width)
def draw_circle(x, y): # o is player 2
    pygame.draw.circle(screen, green, (x*200 + 100, y*200 + 100), 75, line_width)

def draw_moves():
    x_pos = 0
    for x in moves:
        y_pos = 0
        for y in x:
            if y == 1:
                draw_x(x_pos, y_pos)
            if y == 2:
                draw_circle(x_pos, y_pos)
            y_pos += 1
        x_pos += 1

def reset_game():
    global moves
    global player
    moves = [[0,0,0], [0,0,0], [0,0,0]]
    player = 1

run = True

while run:
    
    draw_grid()
    draw_moves()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            x_position = position[0] // 200
            y_position = position[1] // 200
            if moves[x_position][y_position] == 0:
                moves[x_position][y_position] = player
                if player == 1:
                    player = 2
                else:
                    player = 1
            print(moves)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
    pygame.display.update()

pygame.quit()
print('Thanks for playing')