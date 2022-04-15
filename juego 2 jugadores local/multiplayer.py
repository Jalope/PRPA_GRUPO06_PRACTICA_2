# KidsCanCode - Game Development with pg video series
# kidscancode.org/lessons
import pygame as pg
import random
from os import path


#Graphics directory
img_dir = path.join(path.dirname(__file__), 'img')


WIDTH = 960
HEIGHT = 600
FPS = 60


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pg and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Practica3_G06")
clock = pg.time.Clock()

font_name = pg.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def new_mob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
    
def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def show_go_screen(winner):
    screen.blit(background, background_rect)
    if winner == 0:
        draw_text(screen, "MORTAL SPACE KOMBAT!", 64, WIDTH / 2, HEIGHT / 4)
    if winner == 1:
        draw_text(screen, "PLAYER 1 WINS!", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Play again?", 18, WIDTH / 2, HEIGHT * 3 / 4 -20)
    if winner == 2:
        draw_text(screen, "PLAYER 2 WINS!", 64, WIDTH / 2, HEIGHT / 4)
        draw_text(screen, "Play again?", 18, WIDTH / 2, HEIGHT * 3 / 4 -20)
    draw_text(screen, "P1: up, down arrow keys to move, space to fire", 22, WIDTH / 2, HEIGHT / 2-15)
    draw_text(screen, "P2: w, s keys to move, m to fire", 22, WIDTH / 2, HEIGHT / 2+15)
    draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pygame.quit()
            if event.type == pg.KEYUP:
                waiting = False
                
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 21
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = 20
        self.rect.bottom = HEIGHT/2
        self.speedy = 0
        self.live = 3

    def update(self):
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.speedy = -8
        if keystate[pg.K_DOWN]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, 1)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Player2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(player2_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 21
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH-20
        self.rect.bottom = HEIGHT/2
        self.speedy = 0
        self.live = 3

    def update(self):
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.speedy = -8
        if keystate[pg.K_s]:
            self.speedy = 8
        self.rect.y += self.speedy
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, 2)
        all_sprites.add(bullet)
        bullets.add(bullet)
    
class Mob(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*.9 / 2)
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, p):
        pg.sprite.Sprite.__init__(self)
        if p == 1:
            self.image = bullet_img
        if p == 2:
            self.image = bullet2_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        if p == 1:
            self.rect.bottom = y +25
            self.rect.centerx = x +40
        if p == 2:
            self.rect.bottom = y +25
            self.rect.centerx = x -40
        self.speedx = 15
        self.player = p
        
    def update(self):
        if self.player == 1:
            self.rect.x += self.speedx
        else:
            self.rect.x -= self.speedx
        # kill if it moves off the top of the screen
        if (self.rect.right > WIDTH) or (self.rect.left < 0):
            self.kill()
#Load graphics
background = pg.image.load(path.join(img_dir, "b.png")).convert()
background_rect = background.get_rect() 
player_img = pg.image.load(path.join(img_dir, "playerShip3_orange.png")).convert()
player2_img = pg.image.load(path.join(img_dir, "playerShip3_blue.png")).convert()
meteor_img = pg.image.load(path.join(img_dir, "meteorBrown_big3.png")).convert()
bullet_img = pg.image.load(path.join(img_dir, "laserRed16.png")).convert()
bullet2_img = pg.image.load(path.join(img_dir, "laserRed17.png")).convert()
player_mini_img = pg.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)
player2_mini_img = pg.transform.scale(player2_img, (25, 19))
player2_mini_img.set_colorkey(BLACK)        

# Game loop probably need a main function

#start_pos = n.get_pos()
winner = 0
game_over = True
running = True
while running:
    if game_over:
        show_go_screen(winner)
        game_over = False
        all_sprites = pg.sprite.Group()
        mobs = pg.sprite.Group()
        bullets = pg.sprite.Group()
        player = Player()
        player2 = Player2()
        all_sprites.add(player)
        all_sprites.add(player2)

# =============================================================================
#         for i in range(8):
#            new_mob()
# =============================================================================
        
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()
            if event.key == pg.K_m:
                player2.shoot()
    # Update
    all_sprites.update()
# =============================================================================
#     #check if any bullet hit any mob
#     hits = pg.sprite.groupcollide(mobs, bullets, True, True)
#     for hit in hits:
#         score += 1
#         new_mob()
# =============================================================================
    #check to see if a mob hit the player
    hits = pg.sprite.spritecollide(player, mobs, True, pg.sprite.collide_circle)
    for hit in hits:
        player.live -= 1
        new_mob()
        if player.live <= 0:
            game_over = True	
    hits = pg.sprite.spritecollide(player, bullets, True)
    for hit in hits:
        player.live -= 1
        if player.live <= 0:
            winner = 2
            game_over = True
    hits = pg.sprite.spritecollide(player2, bullets, True)
    for hit in hits:
        player2.live -= 1
        if player2.live <= 0:
            winner = 1
            game_over = True
    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_lives(screen, 10, 5, player.live, player_mini_img)
    draw_lives(screen, WIDTH - 100, 5, player2.live, player2_mini_img)
    # *after* drawing everything, flip the display
    pg.display.flip()
    
pg.quit()


