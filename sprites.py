import pygame as pg
from random import randint
from pygame import mixer
pg.mixer.init()
vec = pg.math.Vector2


spiller_img = pg.image.load("spiler.png")
spiller_img = pg.transform.scale(spiller_img,(60,70))
fiende_img = pg.image.load("astroide.png")
fiende_img = pg.transform.scale(fiende_img,(200,200))
kamikaze_img = pg.image.load("asroide2.png")
kamikaze_img = pg.transform.scale(kamikaze_img,(110,110))
chaser_img = pg.image.load("badwing.png")
chaser_img = pg.transform.scale(chaser_img,(80,120))
healing_img = pg.image.load("healing.png")
healing_img = pg.transform.scale(healing_img, (50, 50))
bullet_img = pg.image.load("pang.png")
bullet_img = pg.transform.scale(bullet_img, (15, 35))
score_img = pg.image.load("xp.png")
score_img = pg.transform.scale(score_img, (40, 40))
boss_img = pg.image.load("badwingboss.png")
boss_img = pg.transform.scale(boss_img, (600, 700))
boss_img = pg.transform.rotate(boss_img, 180 )
kamikaze_img = pg.transform.rotate(kamikaze_img, 180 )

skyte = mixer.Sound("Laser_Shoot3.wav")


death1 = pg.image.load("Explosion3/0003.png")
death1 = pg.transform.scale(death1, (200, 200)) 
death2 = pg.image.load("Explosion3/0004.png")
death2 = pg.transform.scale(death2, (200, 200)) 
death3 = pg.image.load("Explosion3/0005.png")
death3 = pg.transform.scale(death3, (200, 200)) 
death4 = pg.image.load("Explosion3/0006.png")
death4 = pg.transform.scale(death4, (200, 200)) 
death5 = pg.image.load("Explosion3/0007.png")
death5 = pg.transform.scale(death5, (200, 200)) 
death6 = pg.image.load("Explosion3/0008.png")
death6 = pg.transform.scale(death6, (200, 200)) 
death7 = pg.image.load("Explosion3/0009.png")
death7 = pg.transform.scale(death7, (200, 200)) 
death8 = pg.image.load("Explosion3/0010.png")
death8 = pg.transform.scale(death8, (200, 200))  
death9 = pg.image.load("Explosion3/0011.png")
death9 = pg.transform.scale(death9, (200, 200)) 
death10 = pg.image.load("Explosion3/0012.png")
death10 = pg.transform.scale(death10, (200, 200)) 
death11 = pg.image.load("Explosion3/0013.png")
death11 = pg.transform.scale(death11, (200, 200)) 
death12 = pg.image.load("Explosion3/0014.png")
death12 = pg.transform.scale(death12, (200, 200)) 
death13 = pg.image.load("Explosion3/0015.png")
death13 = pg.transform.scale(death13, (200, 200)) 
death14 = pg.image.load("Explosion3/0016.png")
death14 = pg.transform.scale(death14, (200, 200)) 
death15 = pg.image.load("Explosion3/0017.png")
death15 = pg.transform.scale(death15, (200, 200)) 
death16 = pg.image.load("Explosion3/0018.png")
death16 = pg.transform.scale(death16, (200, 200)) 
death17 = pg.image.load("Explosion3/0019.png")
death17 = pg.transform.scale(death17, (200, 200)) 
death18 = pg.image.load("Explosion3/0020.png")
death18 = pg.transform.scale(death18, (200, 200)) 
death19 = pg.image.load("Explosion3/0021.png")
death19 = pg.transform.scale(death19, (200, 200)) 
death20 = pg.image.load("Explosion3/0022.png")
death20 = pg.transform.scale(death20, (200, 200)) 

class explosion(pg.sprite.Sprite):
    def __init__(self, game, x, y): # blir gjort da spillet starter
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = death1
        self.rect = self.image.get_rect() # henter self.image sin størrelse
        self.pos = vec(x, y)
        self.rect.center = self.pos
        
        self.current_frame = 0   # lag denne variabelen for exsplosjon spriten
        self.last_update = 0    # trenger begge disse

        self.explode = True

        self.explosion_frames = [death1, death2, death3, death4, death5, death6, death7, death8, death9, death10, death11, death12, death13, death14, death15, death16, death17,death18,death19,death20]

    def animate(self):
        nu = pg.time.get_ticks()   # på starten av animate henter vi hvilken "tick" eller frame vi er på 1 tick er 1 FPS
        if self.explode == True:
            if nu - self.last_update > 50:
                self.last_update = nu
                self.current_frame = (self.current_frame + 1) % len(self.explosion_frames)
                self.image = self.explosion_frames[self.current_frame]
                self.speed = 2
                self.rect = self.image.get_rect()
                


    def update(self):
        self.animate()
        self.rect.center = self.pos
        self.pos.y += self.speed

class bullet(pg.sprite.Sprite):
    def __init__(self, spiller, game):
        pg.sprite.Sprite.__init__(self)
        self.spiller = spiller
        self.game = game
        self.game.all_sprites.add(self)
        self.game.projectile_group.add(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.pos = vec(self.spiller.pos.x, self.spiller.pos.y)
        self.rect.center = self.pos
        self.speed = 5



    def update(self):
        self.rect.y -= 5        

class spiller(pg.sprite.Sprite):
    def __init__(self, game): # blir gjort da spillet starter
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = spiller_img
        self.rect = self.image.get_rect() # henter self.image sin størrelse
        self.pos = vec(400, 500)
        self.rect.center = self.pos
        self.speed = 9
        self.liv = 3

        

   

    

    def update(self):
        self.rect.center = self.pos # flytter spiller til ny posisjon
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.pos.x += self.speed
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_a]:
            self.pos.x -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed

        if keys[pg.K_SPACE]:
            self.shoot_bullet()

       

        
            

        if self.pos.x > 800:
            self.pos.x = 800
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y > 950:
            self.pos.y = 950
        if self.pos.y < 0:
            self.pos.y = 0

    def shoot_bullet(self):
        bullet(self, self.game)
        mixer.Sound.play(skyte)

    



class astroide(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = fiende_img
        self.rect = self.image.get_rect()
        self.pos = vec(-100, 100)
        self.rect.center = self.pos
        self.speed = 2
        self.angle = 0
        self.liv = 570

    def update(self):
        self.rect.center = self.pos # flytter spiller til ny posisjon
        self.pos.y += self.speed
        self.rect.center = self.pos
        
        self.angle += 0.3
 
        self.image, self.rect = self.rot_center(fiende_img, self.angle, self.pos.x, self.pos.y)
       
        if self.pos.y > 1000:
            self.pos.y = -100
            self.pos.x = randint(0,800)

        if self.liv <= 0:
            self.kill()


    def rot_center(self, image, angle, x, y):   
        rotated_image = pg.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (x, y)).center)
 
        return rotated_image, new_rect

    

class kamikaze(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = kamikaze_img
        self.rect = self.image.get_rect()
        self.pos = vec(-100, 100)
        self.rect.center = self.pos
        self.speed = 5
        self.angle = 0
        self.liv = 250


    def update(self):
        self.rect.center = self.pos # flytter spiller til ny posisjon
        self.pos.y += self.speed

        if self.pos.y > 1000:
            self.pos.y = -100
            self.pos.x = randint(0,800)
        self.angle += 1
 
        self.image, self.rect = self.rot_center(kamikaze_img, self.angle, self.pos.x, self.pos.y)
       
        if self.pos.y > 1000:
            self.pos.y = -100
            self.pos.x = randint(0,800)
        if self.liv <= 0:
            self.kill()
            

    def rot_center(self, image, angle, x, y):   
        rotated_image = pg.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (x, y)).center)
 
        return rotated_image, new_rect



        
        
    



class chaser(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        #self.game = game
        self.image = chaser_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(200, 800), 1000)
        self.rect.center = self.pos
        self.speed = 7
        self.right = False
        self.max_height = randint(600,800)
        self.current_frame = 0
        self.last_frame = 0
        self.liv = 100
        print (self.liv)


    def update(self):
        self.rect.center = self.pos # flytter spiller til ny posisjon
        self.pos.y -= self.speed
        
        

        if self.right == False and self.pos.y < self.max_height:
            self.speed = 0
            self.pos.x -= 1
        if self.pos.x < 100:
            self.right = True
        if self.right == True:
            self.speed = 0
            self.pos.x += 1
        if self.pos.x > 700:
            self.right = False

        if self.liv <= 0:
            self.kill()


class healing_orb(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = healing_img
        self.rect = self.image.get_rect()
        self.pos = vec(-100, 100)
        self.rect.center = self.pos
        self.speed = 2
        self.angle = 0

    def update(self):
        self.rect.center = self.pos # flytter spiller til ny posisjon
        self.pos.y += self.speed

        if  self.pos.y > 1000:
                self.pos.y = -100
                self.pos.x = randint(0,800)
            
        self.angle += 1

        
    
        self.image, self.rect = self.rot_center(healing_img, self.angle, self.pos.x, self.pos.y)
    
    def rot_center(self, image, angle, x, y):   
        rotated_image = pg.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (x, y)).center)
 
        return rotated_image, new_rect






class scoreorb(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = score_img
        self.rect = self.image.get_rect()
        self.pos = vec(-100, 100)
        self.rect.center = self.pos
        self.speed = 9
        self.angle = 0

    def update(self):
        self.rect.center = self.pos # flytter spiller til ny posisjon
        self.pos.y += self.speed
        

        if self.pos.y > 1000:
            self.pos.y = -100
            self.pos.x = randint(0,800)
        self.angle += 8

        self.image, self.rect = self.rot_center(score_img, self.angle, self.pos.x, self.pos.y)
    
    def rot_center(self, image, angle, x, y):   
        rotated_image = pg.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect(center = (x, y)).center)
 
        return rotated_image, new_rect


class boss(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = boss_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(800, 1000),  100)
        self.rect.center = self.pos
        self.speed = 0.3
        self.right2 = False
        self.max_height = randint(100,100)

    def update(self):
        self.rect.center = self.pos # flytter spiller til ny posisjon
        self.pos.y -= self.speed
        
        

        if self.right2 == False and self.pos.y < self.max_height:
            self.speed = 0
            self.pos.x -= 0.3
        if self.pos.x < 100:
            self.right2 = True
        if self.right2 == True:
            self.speed = 0
            self.pos.x += 0.3
        if self.pos.x > 700:
            self.right2 = False

    def animate(self):
        now = pg.time.get_ticks()
        if self.dead == True:
            if now - self.last_update > 350:   # her sørger vi for at vi bytte bilde kun hver 350 tick, lavere tall animerer fortere
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.deads)
                self.image = self.dead[self.current_frame]
                self.rect = self.image.get_rect()
           

                


            

            

       


    
            
       