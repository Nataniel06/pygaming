import pygame as pg
from random import randint

pg.init()

HVIT = (255,255,255)
SVART = (0,0,0)
BLÅ = (0,0,255)
box_farge = (255,255,255)
skjerm = pg.display.set_mode((800,1000))


fps_teller = 0
x  = 270
y = 1000

spiller_img = pg.image.load("f-15.png")
spiller_img = pg.transform.scale(spiller_img,(200,230))




direksjon_x = 0
direksjon_y = 0

FPS = 120
klokke = pg.time.Clock()
fart = 5

gaming = True
while gaming:
    klokke.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gaming = False
    farge= (randint(0,255),randint(0,255),randint(0,255))
    skjerm.fill(SVART)

    keys = pg.key.get_pressed()
    if keys[pg.K_d]:
        x += fart
    if keys[pg.K_w]:
        y -= fart
    if keys[pg.K_a]:
        x -= fart
    if keys[pg.K_s]:
        y += fart

    if x > 750:
        box_farge = (255,0,0)
    if x < 0:
        box_farge = (0,255,0)
    if y > 450:
        box_farge = (0,0,255)
    if y < 0:
        box_farge = (255,255,0)



    if x > 750:
        x = 750
    if x < 0:
        x = 0
    if y > 950:
        y = 950
    if y < 0:
        y = 0

    skjerm.blit(spiller_img, ( x, y ))
      



    


    


    


    pg.display.update()

    

