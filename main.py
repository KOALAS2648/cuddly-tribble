
import pygame as pg
import math
pg.init()
font = pg.font.Font(None, 32)
screen = pg.display.set_mode((1800, 800))
clock = pg.time.Clock()
done = False
x,y = 150,350
x2,y2 = 0+25,350
x3,y3 = 0,350
x4, y4 = 350, 0
wave_speed = 0.1
multiplier = 100
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.fill((255, 255, 255))
    text = font.render('sin wave', True, (0, 0, 0))
    text2 = font.render('cos wave', True, (0, 0, 0))
    text3 = font.render('tan wave', True, (0, 0, 0))
    text4 = font.render("sin wave: y", True, (0,0,0), (255, 255, 0))
    y = math.sin(wave_speed) * multiplier    
    y2 = math.cos(wave_speed) *multiplier
    y3 = math.tan(wave_speed) *multiplier
    x4 = math.sin(wave_speed) * multiplier
    screen.blit(text, (x, y+400))
    screen.blit(text2, (x2, y2+400))
    screen.blit(text3, (x3, y3+400))
    screen.blit(text4, (x4+400, y4))
    x +=1
    x2 +=1
    x3 +=1
    y4 +=1
    if x > 1800:
        x = 0
    if x2 > 1800:
        x2 = 0
    if x3 > 1800:
        x3 = 0
    if y4 > 800:
        y4 = 0
    wave_speed += 0.1
    pg.display.flip()
    clock.tick(60)

print("hello world")