import pygame as pg

GREEN = (0,255,0)

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, c):
        pg.sprite.Sprite.__init__(self)
        self.score = 0
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.color = c
        self.rect = (x,y,w,h)
        self.speed = 3
        self.bullets = pg.sprite.Group()
		self.hitbox = (x,y,w,h)

    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)
        pg.draw.rect(win, GREEN, self.rect,2)
        for b in self.bullets:
            b.draw(win)
    
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
    
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.bullets.update()
        for b in self.bullets:
            b.update()
        
            
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        if y == 550: 
            self.side = 1
        else:
            self.side = 0
        self.x = x+20
        if self.side == 1:
            self.y = y-26
        else:
            self.y = y+51
        self.color = GREEN 
        self.rect = (x,y,10,20)
        self.speed = -3
        
        
    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)

    def update(self):
        if self.side == 1:
            self.y += self.speed
        else:
            self.y -= self.speed
        if self.y > 580:
            self.kill()
        if self.y < 1:
            self.kill()
        self.rect = (self.x, self.y, 10, 20)
