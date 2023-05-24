import pygame as pg
from random import randint
vec = pg.math.Vector2

percent = 38
width = 600/100*percent
if width < 120:
    width = 120/600
else:
    width = width/600
height = width

WIDTH = 600 * width
HEIGHT = 600 * height

RED = (255,0,0)

class Munn(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.size = vec(230 * width,5 * height)
        self.image = pg.Surface(self.size)
        self.image.fill((50,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.rect.midtop = self.pos
        self.realspeed = 20 * width
        self.mouse_on = False
        self.mouse_off = False
        self.not_mm = False
        self.talk = False
        self.move_to = vec(200 * width,5 * height)
        self.move_vector = vec(1,1)

        self.last_update = 0
        self.last_snorkate = 0
        self.snork_sycle = 1
        self.zzz = False

        self.aa = vec(230 * width,170 * height)
        self.ee = vec(300 * width,130 * height)
        self.ii = vec(350 * width,90 * height)
        self.oo = vec(70 * width,100 * height)
        self.uu = vec(60 * width,110 * height)
        self.yy = vec(105 * width,105 * height)
        self.ææ = vec(280 * width,170 * height)
        self.øø = vec(110 * width,110 * height)
        self.åå = vec(140 * width,150 * height)
        self.mm = vec(400 * width,5 * height)
        self.qq = vec(WIDTH-(175*width), (HEIGHT/2)-(30*height))
        self.space = vec(230 * width,5 * height)
        
    
    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LCTRL]:
            self.mouse_on = True
        elif keys[pg.K_LALT]:
            self.mouse_on = False

        if keys[pg.K_t] and not self.talk:
            self.talk = True

        if keys[pg.K_z] and not self.zzz:
            self.zzz = True

        if keys[pg.K_s] and (self.talk or self.zzz):
            self.talk = False
            self.zzz = False



        
        if keys[pg.K_1]:
            self.realspeed = 1 * width
        if keys[pg.K_2]:
            self.realspeed = 5 * width
        if keys[pg.K_3]:
            self.realspeed = 20 * width
        self.speed = self.realspeed

        self.rect.midtop = self.pos
        if keys[pg.K_a]:
            self.move_to = vec(self.aa)
        
        elif keys[pg.K_e]:
            self.move_to = vec(self.ee)
        
        elif keys[pg.K_i]:
            self.move_to = vec(self.ii)

        elif keys[pg.K_o] or keys[pg.K_w]:
            self.move_to = vec(self.oo)

        elif keys[pg.K_u]:
            self.move_to = vec(self.uu)
        
        elif keys[pg.K_y]:
            self.move_to = vec(self.yy)

        elif keys[pg.K_j]:
            self.move_to = vec(self.ææ)

        elif keys[pg.K_k]:
            self.move_to = vec(self.øø)

        elif keys[pg.K_l]:
            self.move_to = vec(self.åå)

        elif keys[pg.K_q]:
            self.move_to = vec(self.qq)

        elif keys[pg.K_m]:
            self.move_to = vec(self.mm)
            self.not_mm = True

        elif self.not_mm:
            if self.size.x != 230 * width:
                self.move_to.x = 230 * width

            else:
                self.not_mm = False

        elif keys[pg.K_SPACE]:
            self.move_to = vec(self.space)

        elif self.mouse_on:
            self.speed = 40 * width
            self.mouse = vec(pg.mouse.get_pos())
            self.mouse.x = (self.mouse.x - self.pos.x) * 2
            if self.mouse.x < 0:
                self.mouse.x = self.mouse.x*-1
            if self.mouse.x == 0:
                self.mouse.x = 1

            if self.mouse.y < self.pos.y + 5 * height:
                self.mouse.y = self.pos.y + 5 * height

            self.move_to = vec(self.mouse.x, self.mouse.y - self.pos.y)
        
        elif self.talk:
            self.snakk()

        elif self.zzz:
            self.snork()

        else:
            self.move_to = vec(self.size.x, 5 * height)

        self.move_vector = self.move_to - self.size

        if self.move_vector.x == 0:
            self.move_vector.x = 1
        if self.move_vector.y == 0:
            self.move_vector.y = 1
        self.move_vector = self.move_vector.normalize()


        if self.size.y != self.move_to.y:
            self.size.y += self.speed * self.move_vector.y

        if self.size.y < self.move_to.y + self.speed and self.size.y > self.move_to.y - self.speed:
            self.size.y = self.move_to.y

        
        if self.size.x != self.move_to.x:
            self.size.x += self.speed * self.move_vector.x

        if self.size.x < self.move_to.x + self.speed and self.size.x > self.move_to.x - self.speed:
            self.size.x = self.move_to.x

        if keys[pg.K_TAB]:
            print(self.move_vector.y)


        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.midtop = self.pos
    

    def snakk(self):
        self.now = pg.time.get_ticks()
        if self.size == self.move_to:
            self.rand = randint(1,120)
            self.rand2 = randint(1,2)
        if self.now - self.last_update > randint(60,90):
            self.last_update = self.now
            if self.rand <= 30:
                if self.rand2 == 1:
                    self.move_to = vec(self.aa)
                if self.rand2 == 2:
                    self.move_to = vec(self.ææ)

            elif self.rand <= 60:
                if self.rand2 == 1:
                    self.move_to = vec(self.ii)
                if self.rand2 == 2:
                    self.move_to = vec(self.ee)

            elif self.rand <= 80:
                if self.rand2 == 1:
                    self.move_to = vec(self.oo)
                if self.rand2 == 2:
                    self.move_to = vec(self.åå)

            elif self.rand <= 81:
                self.move_to = vec(self.qq)
                
            else:
                self.move_to = vec(self.size.x, 5 * height)

    

    def snork(self):
        self.now = pg.time.get_ticks()

        if self.snork_sycle == 5:
            self.snork_sycle = 1

        if self.now - self.last_update > 600 and (self.snork_sycle == 1 or self.snork_sycle == 3):
            self.last_update = self.now
            if self.snork_sycle == 1:
                self.move_to = vec(self.ææ)
            elif self.snork_sycle == 3:
                self.move_to = vec(self.oo)
            self.snork_sycle += 1

        elif self.now - self.last_update > 1450:
            self.last_update = self.now
            self.move_to = vec(self.size.x + (20 * width), 50 * height)
            self.snork_sycle += 1



class Øyne(pg.sprite.Sprite):
    def __init__(self, game, side):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.size = vec(20 * width,20 * width)
        self.image = pg.Surface(self.size)
        self.image.fill((0,0,20))
        self.rect = self.image.get_rect()
        if side == 1:
            self.pos = vec(WIDTH/7, HEIGHT/6)
            self.main_pos = vec(WIDTH/7, HEIGHT/6)
        if side == 2:
            self.pos = vec(WIDTH/1.15, HEIGHT/3)
            self.main_pos = vec(WIDTH/1.15, HEIGHT/3)
        self.main_mouse = vec(WIDTH/2, HEIGHT/4)
        self.rect.center = self.pos
        self.speed = 4 * width
        self.blink = False
        self.move_to = vec(200 * width,5 * height)
        self.move_vector = vec(1,1)

        self.talk = False
        self.rand = 0
        self.look = False

        self.toggle = False

        self.last_update = 0

    def update(self):
        keys = pg.key.get_pressed()
        self.now = pg.time.get_ticks()

        self.rect.center = self.pos
        
        if keys[pg.K_t] and not self.talk:
            self.talk = True
        elif keys[pg.K_s] and self.talk:
            self.talk = False

        if keys[pg.K_PLUS]:
            self.look = True
        elif keys[pg.K_BACKSLASH]:
            self.look = False


        if (keys[pg.K_DOWN] or (keys[pg.K_LSHIFT] and keys[pg.K_z])) and not keys[pg.K_UP] and self.pos.y < self.main_pos.y + 60 * height:
            self.pos.y += self.speed 
        elif keys[pg.K_UP] and self.pos.y > self.main_pos.y - 60 * height:
            self.pos.y -= self.speed 

        if keys[pg.K_LEFT] and not keys[pg.K_RIGHT] and self.pos.x > self.main_pos.x - 60 * width:
            self.pos.x -= self.speed
        elif keys[pg.K_RIGHT] and self.pos.x < self.main_pos.x + 60 * width:
            self.pos.x += self.speed
        
        if keys[pg.K_RCTRL] or (keys[pg.K_LSHIFT] and keys[pg.K_z]):
            self.toggle = True
        elif keys[pg.K_RSHIFT]:
            self.toggle = False
        
        if keys[pg.K_b] or (keys[pg.K_LSHIFT] and keys[pg.K_z]):
            self.blink = True
        
        if keys[pg.K_MINUS] or self.blink or (self.talk and self.size.y > 5 * width and self.game.rand == 23):
            if self.size.y > 5 * width:
                self.size.y -= 5 * width
            elif self.size.y <= 5 * width:
                self.size.y = 5 * width
            if keys[pg.K_MINUS]:
                self.blink = False
        elif self.size.y < 20 * width and not self.blink:
            self.size.y += 5 * width
        elif self.size.y > 20 * width:
            self.size.y = 20 * width
            

        if not self.toggle:

            if self.look:
                self.move_to = vec(pg.mouse.get_pos())
                self.move_to.y -= self.main_mouse.y - self.main_pos.y
                self.move_to.x -= self.main_mouse.x - self.main_pos.x

            else:
                self.move_to = vec(self.main_pos)

            self.move_vector = self.move_to - self.pos

            if self.move_vector.x == 0:
                self.move_vector.x = 1
            if self.move_vector.y == 0:
                self.move_vector.y = 1
            self.move_vector = self.move_vector.normalize()

            if self.look:

                self.pos.y += (self.speed*20)  * self.move_vector.y
                
                if self.pos.y < self.move_to.y + (self.speed*20) and self.pos.y > self.move_to.y - (self.speed*20):
                    self.pos.y = self.move_to.y
                
                if self.pos.y > self.main_pos.y + 60 * height:
                    self.pos.y = self.main_pos.y + 60 * height
                elif self.pos.y < self.main_pos.y - 60 * height:
                    self.pos.y = self.main_pos.y - 60 * height


                self.pos.x += (self.speed*20)  * self.move_vector.x
                
                if self.pos.x < self.move_to.x + (self.speed*20) and self.pos.x > self.move_to.x - (self.speed*20):
                    self.pos.x = self.move_to.x

                if self.pos.x > self.main_pos.x + 60 * width:
                    self.pos.x = self.main_pos.x + 60 * width
                elif self.pos.x < self.main_pos.x - 60 * width:
                    self.pos.x = self.main_pos.x - 60 * width
                    
            
            else:
                if self.pos.y != self.move_to.y and not (keys[pg.K_UP] or keys[pg.K_DOWN]):
                    self.pos.y += self.speed * self.move_vector.y
                if self.pos.y < self.move_to.y + self.speed and self.pos.y > self.move_to.y - self.speed and not (keys[pg.K_UP] or keys[pg.K_DOWN]):
                    self.pos.y = self.move_to.y

                
                if self.pos.x != self.move_to.x and not (keys[pg.K_LEFT] or keys[pg.K_RIGHT]):
                    self.pos.x += self.speed * self.move_vector.x
                if self.pos.x < self.move_to.x + self.speed and self.pos.x > self.move_to.x - self.speed and not (keys[pg.K_LEFT] or keys[pg.K_RIGHT]):
                    self.pos.x = self.move_to.x



        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos