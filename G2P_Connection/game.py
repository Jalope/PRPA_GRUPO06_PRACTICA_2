import pygame as pg

WIDTH = 300
HEIGHT = 600

GREEN = (0,255,0)
P_COLOR1 = (5,123,219)
P_COLOR2 =  (0,0,0)

class Game():
    def __init__(self, id):
        self.id = id
        self.players = [Player(0,0,50,50,P_COLOR1), Player(0,550,50,50,P_COLOR2)]
        self.ready = False
        self.p1_wins = False
        self.p2_wins = False
    
    def connected(self):
        return self.ready
    
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
        

    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)
        pg.draw.rect(win, GREEN, self.rect,2) #hitbox
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
        self.speed = -4
             
    def draw(self, win):
        pg.draw.rect(win, self.color, self.rect)

    def update(self):
        if self.side == 1:
            self.y += self.speed
        else:
            self.y -= self.speed
        if self.y > HEIGHT-20:
            self.kill()
        if self.y < 1:
            self.kill()
        self.rect = (self.x, self.y, 10, 20)
