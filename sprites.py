import pygame as pg
from random import randint
vec = pg.math.Vector2

WIDTH = 600
HEIGHT = 600

RED = (255,0,0)

class Munn(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.size = vec(230,5)
        self.image = pg.Surface(self.size)
        self.image.fill((50,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.rect.midtop = self.pos
        self.realspeed = 20
        self.mouse_on = False
        self.mouse_off = False
        self.not_mm = False
        self.move_to = vec(200,5)
        self.move_vector = vec(1,1)

        self.aa = vec(230,170)
        self.ee = vec(300,130)
        self.ii = vec(350,90)
        self.oo = vec(70,100)
        self.uu = vec(60,110)
        self.yy = vec(105,105)
        self.ææ = vec(280,170)
        self.øø = vec(110,110)
        self.åå = vec(140,150)
        self.mm = vec(400,5)
        
    
    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_LCTRL]:
            self.mouse_on = True
        elif keys[pg.K_LALT]:
            self.mouse_on = False

        
        if keys[pg.K_1]:
            self.realspeed = 1
        if keys[pg.K_2]:
            self.realspeed = 5
        if keys[pg.K_3]:
            self.realspeed = 20
        self.speed = self.realspeed

        self.rect.midtop = self.pos
        if keys[pg.K_a]:
            self.move_to = vec(self.aa)
            self.move_vector = self.move_to - self.size
        
        elif keys[pg.K_e]:
            self.move_to = vec(self.ee)
            self.move_vector = self.move_to - self.size
        
        elif keys[pg.K_i]:
            self.move_to = vec(self.ii)
            self.move_vector = self.move_to - self.size

        elif keys[pg.K_o]:
            self.move_to = vec(self.oo)
            self.move_vector = self.move_to - self.size

        elif keys[pg.K_u]:
            self.move_to = vec(self.uu)
            self.move_vector = self.move_to - self.size
        
        elif keys[pg.K_y]:
            self.move_to = vec(self.yy)
            self.move_vector = self.move_to - self.size

        elif keys[pg.K_j]:
            self.move_to = vec(self.ææ)
            self.move_vector = self.move_to - self.size

        elif keys[pg.K_k]:
            self.move_to = vec(self.øø)
            self.move_vector = self.move_to - self.size

        elif keys[pg.K_l]:
            self.move_to = vec(self.åå)
            self.move_vector = self.move_to - self.size

        elif keys[pg.K_m]:
            self.move_to = vec(self.mm)
            self.move_vector = self.move_to - self.size
            self.not_mm = True

        elif self.not_mm:
            if self.size.x != 230:
                self.move_to.x = 230
                self.move_vector = self.move_to - self.size
            else:
                self.not_mm = False

        elif self.mouse_on:
            self.speed = 10000
            self.mouse = vec(pg.mouse.get_pos())
            self.mouse.x = (self.mouse.x - self.pos.x) * 2
            if self.mouse.x < 0:
                self.mouse.x = self.mouse.x*-1
            if self.mouse.x == 0:
                self.mouse.x = 1

            if self.mouse.y < self.pos.y + 5:
                self.mouse.y = self.pos.y + 5

            self.move_to = vec(self.mouse.x, self.mouse.y - self.pos.y)
            self.move_vector = self.move_to - self.size

        else:
            self.move_to = vec(self.size.x, 5)
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

        if keys[pg.K_LSHIFT]:
            print(self.move_vector.y)


        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.midtop = self.pos


class Øyne(pg.sprite.Sprite):
    def __init__(self, game, side):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.size = vec(20,20)
        self.image = pg.Surface(self.size)
        self.image.fill((0,0,20))
        self.rect = self.image.get_rect()
        if side == 1:
            self.pos = vec(WIDTH/7, HEIGHT/6)
            self.main_pos = vec(WIDTH/7, HEIGHT/6)
        if side == 2:
            self.pos = vec(WIDTH/1.15, HEIGHT/3)
            self.main_pos = vec(WIDTH/1.15, HEIGHT/3)
        self.rect.center = self.pos
        self.realspeed = 20
        self.move_to = vec(200,5)
        self.move_vector = vec(1,1)

    def update(self):
        keys = pg.key.get_pressed()

        self.rect.center = self.pos

        if keys[pg.K_DOWN] and self.pos.y < self.main_pos.y + 20:
            self.pos.y += 5
        if keys[pg.K_UP] and self.pos.y > self.main_pos.y - 20:
            self.pos.y -= 5

        
        if keys[pg.K_LEFT] and self.pos.x > self.main_pos.x - 20:
            self.pos.x -= 5
        if keys[pg.K_RIGHT] and self.pos.x < self.main_pos.x + 20:
            self.pos.x += 5

        self.rect.center = self.pos