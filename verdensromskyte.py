import pygame as pg
from random import randint
from sprites import *
from pygame import mixer














class game():
    def __init__(self): # kjører når vi starter spillet
        pg.init()
        self.skjerm = pg.display.set_mode((800,1000))
        self.bg = pg.image.load("bg12.png")
        self.bg = pg.transform.scale(self.bg,(1000, 1000))
        self.skjerm = pg.display.set_mode((800,1000))
        self.comic_sans30 = pg.font.SysFont("Times New Roman", 30)
        self.meny_tekst = pg.font.SysFont("Calibri MS", 80)
        self.yanimage = pg.image.load("ssdasdffff.jpg")
        self.yanimage = pg.transform.scale(self.yanimage, (500, 250))
        
        
        self.box_farge = (255,255,255)

        self.HVIT = (255,255,255)
        self.SVART = (0,0,0)
        self.RED = (255, 0 , 0)
        
        self.smerte = mixer.Sound("Explosion9.wav")
        self.pling = mixer.Sound("Powerup8.wav")
        self.pain = mixer.Sound("Hit_Hurt3.wav")

        
        self.FPS = 120
        self.fart = 5 
        self.last_orb_spawn = 0
        self.last_orb_spawn2 = 0
        self.boss_spawn = 0
        self.klokke = pg.time.Clock()

            
        pg.display.update()
        
        self.game_menu()

    def game_menu(self):
    
        mixer.music.stop()
        mixer.music.load("02 Space Enviroment Final.mp3")
        mixer.music.play(-1)

        
     
  
        self.game_over = True
        while self.game_over:
            self.klokke.tick(self.FPS)
            self.menu_text = self.meny_tekst.render("Verdensromskyte the game", False, (self.HVIT))
            self.menu2_text = self.meny_tekst.render("Press E to start", False, (self.HVIT))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()
        


                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_e: 
                        self.new() 
                        self.game_over = False
                        
            self.skjerm.blit (self.bg, (10, 10))

            
            self.skjerm.blit(self.menu_text,(24,100))
            self.skjerm.blit(self.menu2_text,(180,800))  # tegner tekst på skjerm. 
            


            pg.display.update()
            
        



    def new(self): # ny runde, kjører feks når vi dør
        mixer.music.stop()  
        mixer.music.load("4 - Storming Eye.mp3")
        mixer.music.play(-1)

        self.i = 0

        self.gamer = spiller(self)
        self.gog = astroide()
        self.japan = kamikaze()
        self.romania = chaser()
        
        

        self.all_sprites = pg.sprite.Group()
        self.fiende_group = pg.sprite.Group()
        self.healing_group = pg.sprite.Group()
        self.score_group = pg.sprite.Group()
        self.projectile_group = pg.sprite.Group()

        self.all_sprites.add(self.gamer,self.japan,self.romania,self.gog)
        self.fiende_group.add(self.gog, self.japan, self.romania)
        
        

        self.score = 0
     

        self.run()

    def Explosjon(self,x, y):
        self.explosion = explosion(self, x, y)
        self.all_sprites.add(self.explosion)
        mixer.Sound.play(self.smerte)
        pg.display.update()


    def run(self): # mens vi spiller, game loop er her
        gaming = True
        while gaming:
            self.klokke.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    gaming = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.new()
                       
            self.now = pg.time.get_ticks()

            keys = pg.key.get_pressed()
            
            if keys[pg.K_6]: # hard mode. gir spilleren ett liv og setter på ny sang
                mixer.music.stop()
                mixer.music.load("10 - Unsanctified.mp3")
                mixer.music.set_volume(1)
                mixer.music.play(-1)
                self.gamer.liv = 1
                
                
    

            self.farge= (randint(0,255),randint(0,255),randint(0,255))
            
            self.treff_sprite = pg.sprite.spritecollide(self.gamer, self.fiende_group, True)
            if self.treff_sprite:
                self.score -= 100
                self.gamer.liv -= 1 #gjør som at spiller mister liv      
                
                self.Explosjon(self.treff_sprite[0].pos.x, self.treff_sprite[0].pos.y)

 
                if self.gamer.liv <= 0:
                    self.game_stop()

            self.treff2 = pg.sprite.spritecollide(self.gamer, self.healing_group, True)
            if self.treff2:
                self.score += 50
                self.gamer.liv += 1
                mixer.Sound.play(self.pling)
            self.treff3 = pg.sprite.spritecollide(self.gamer, self.score_group, True)
            if self.treff3:
                self.score += 1000
                mixer.Sound.play(self.pling)

            self.treff4 = pg.sprite.groupcollide( self.fiende_group, self.projectile_group, False,True)
            if self.treff4:
                for enemy in self.treff4: 
                    enemy.liv -= 1
                    
                    mixer.Sound.play(self.pain)


                    if enemy.liv <= 0:
                        self.Explosjon(enemy.pos.x, enemy.pos.y)

                self.score += 10  
                
    

                
                
                
            if self.last_orb_spawn + 60000 < self.now:
                self.health_orb = healing_orb()
                self.all_sprites.add(self.health_orb)
                self.healing_group.add(self.health_orb)
                
                self.last_orb_spawn = self.now

            if self.last_orb_spawn2 + 150000 < self.now:
                self.score_orb = scoreorb()
                self.all_sprites.add(self.score_orb)
                self.score_group.add(self.score_orb)
                
                self.last_orb_spawn2 = self.now



            self.skjerm.blit (self.bg, (0, self.i))
            self.skjerm.blit(self.bg, (0, -1000+self.i))
            if (self.i == 1000):
                self.skjerm.blit (self.bg, (0, -1000+self.i))
                self.i=0
            self.i += 1

            if len(self.fiende_group) < 3:
                self.gog = astroide()
                self.all_sprites.add(self.gog)
                self.fiende_group.add(self.gog)
                self.japan = kamikaze()
                self.all_sprites.add(self.japan)
                self.fiende_group.add(self.japan)
                self.romania = chaser()
                self.all_sprites.add(self.romania)
                self.fiende_group.add(self.romania)

           

            self.all_sprites.draw(self.skjerm)
           

            text_player_hp = self.comic_sans30.render("HP: " + str(self.gamer.liv), False, (self.HVIT))
            score_text = self.comic_sans30.render("Score: " + str(self.score), False, (self.HVIT))
            self.skjerm.blit(text_player_hp, (10, 10))
            self.skjerm.blit(score_text, (100, 10))
            self.all_sprites.update()
           
            pg.display.update()


            
    def game_stop(self):
        mixer.music.stop()
        mixer.music.load("5 - Pleasure Is Pain.mp3")
        mixer.music.play(-1)
        self.game_over = True
        while self.game_over:
            self.klokke.tick(self.FPS)
            self.game_over_text = self.comic_sans30.render("Game over, click R to restart", False, (self.RED))
            self.game_over_text2 = self.comic_sans30.render("or click M to go to the startscreen", False, (self.RED))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:  # om vi clicker på R, avslutter vi game over loop, og går derett til self.new() som ligger etter game_over loop
                        self.game_over = False
                        self.new()
 
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:  
                        self.game_over = False
                        self.game_menu()

            self.skjerm.fill(self.SVART)
            self.skjerm.blit(self.game_over_text,(200,100))
            self.skjerm.blit(self.game_over_text2,(200,150))  # tegner tekst på skjerm. 
            score_text = self.comic_sans30.render("Score: " + str(self.score), False, (self.RED))
            self.skjerm.blit(score_text, (200, 200))
        
                

            

            
            pg.display.update()
        
        


g = game()