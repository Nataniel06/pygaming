import pygame as pg
from random import randint
from sprites import *
from pygame import mixer


 
pg.init()

HVIT = (255,255,255)
SVART = (0,0,0)
BLÅ = (0,0,255)

all_sprites = pg.sprite.Group()

fiende_group = pg.sprite.Group()
healing_group = pg.sprite.Group()

gamer = spiller(self)
gog = astroide()
japan = kamikaze()
romania = chaser()


score = 0

mixer.music.load("4 - Storming Eye.mp3")
mixer.music.play(-1)




all_sprites.add(gamer,japan,romania,gog)


fiende_group.add(gog, japan, romania)




bg = pg.image.load("bg12.png")
bg = pg.transform.scale(bg,(1000, 1000))


i = 0 #trengs for scroll bakgrunn

#lag nye fiender hvis de dør

comic_sans30 = pg.font.SysFont("times new roman", 30)
print(gamer.liv)


box_farge = (255,255,255)
skjerm = pg.display.set_mode((800,1000))


fps_teller = 0




direksjon_x = 0
direksjon_y = 0

FPS = 120
klokke = pg.time.Clock()
fart = 5

last_orb_spawn = 0

gaming = True
while gaming:
    klokke.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gaming = False
    
   
    skjerm.blit(bg,(i,7))
    now = pg.time.get_ticks()

    farge= (randint(0,255),randint(0,255),randint(0,255))
    skjerm.fill(SVART) # tegner bakgrunn
    treff = pg.sprite.spritecollide(gamer, fiende_group, True)
    if treff:
        score -= 100
        gamer.liv -= 1 #gjør som at spiller mister liv
        print("LIV: ", gamer.liv)
        if gamer.liv <= 0:
            gamer.kill()
            gamer = spiller()
            all_sprites.add(gamer)

    treff2 = pg.sprite.spritecollide(gamer, healing_group, True)
    if treff2:
        score += 50
        gamer.liv += 1

        
    if last_orb_spawn + 100000 < now:
        health_orb = healing_orb()
        all_sprites.add(health_orb)
        healing_group.add(health_orb)
        print("spawned orb")
        last_orb_spawn = now





    skjerm.blit (bg, (0, i))
    skjerm.blit(bg, (0, -1000+i))
    if (i == 1000):
        skjerm.blit (bg, (0, -1000+i))
        i=0
    i += 1


   



        

    if len(fiende_group) < 3:
        gog = astroide()
        all_sprites.add(gog)
        fiende_group.add(gog)
        japan = kamikaze()
        all_sprites.add(japan)
        fiende_group.add(japan)
        romania = chaser()
        all_sprites.add(romania)
        fiende_group.add(romania)
        
       
        


   

    all_sprites.draw(skjerm) # tegner alle sprites i gruppen all_sprites til skjerm
    text_player_hp = comic_sans30.render("HP: " + str(gamer.liv), False, (HVIT))
    score_text = comic_sans30.render("Score: " + str(score), False, (HVIT))
    skjerm.blit(text_player_hp, (10, 10))
    skjerm.blit(score_text, (100, 10))
    all_sprites.update() # kjør update












    


    


    


    pg.display.update()

    

