import pygame as pg
from sprites_scale import *
print("")


class Game():
    def __init__(self): # kjører når spillet starter
        pg.init()
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.TURT = (255,201,14)


        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.FPS = 120
        self.clock = pg.time.Clock()

        self.new()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.munn = Munn(self)
        self.øye1 = Øyne(self, 1)
        self.øye2 = Øyne(self, 2)
        self.rand = 0
        self.last_update = 0
        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.playing = False
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                self.playing = False
                self.new()
        
            self.screen.fill(self.TURT)

            if self.øye1.talk and self.øye1.now - self.last_update > 70:
                self.last_update = self.øye1.now
                self.rand = randint(1,50)
        
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pg.display.update()



Game()