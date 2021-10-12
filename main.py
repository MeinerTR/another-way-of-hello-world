import pygame as pg

pg.init()
screen = pg.display.set_mode((1600, 900), pg.FULLSCREEN)

font=pg.font.SysFont('Pixellari', 74)

while True:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE: exit()
    screen.blit(font.render('hello world', False, (255, 255, 255)), (((1600/2)-130), (900/2)-24))
    pg.display.update()