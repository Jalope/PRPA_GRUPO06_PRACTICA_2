import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, c):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = c
        self.rect = (x,y,w,h)
        self.speed = 3
        self.bullets = pg.sprite.Group()
    
    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)
    
    def move(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT]:
            self.x -= self.speed
        if keys[pg.K_RIGHT]:
            self.x += self.speed
        
        
        self.update()
        
    def shoot(self):
        bullet = Bullet(self.x, self.y)
        self.bullets.add(bullet)
        return bullet
    
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.bullets.update()
            
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = (0,255,0)
        self.rect = (x,y,10,20)
        self.speed = -3
        
    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)

    def update(self):
        self.y += self.speed