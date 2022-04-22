import pygame as pg
from network import Network

FPS = 60

WIDTH = 300
HEIGHT = 600

WHITE = (255,255,255)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("HIT!")
background = pg.image.load("big.jpg").convert()
background_rect = background.get_rect() 
font_name = pg.font.match_font('arial')

def draw_text(surf, text, size, x, y):
	font = pg.font.Font(font_name, size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)

def display(screen, player1, player2):
    player1.draw(screen)
    player2.draw(screen)
    draw_text(screen, f'score: ({player2.score},{player1.score})', 15, WIDTH/2, HEIGHT/2)
    pg.display.update()

def hit(value,b,p2):#sustituye al método sprite.collide. Adjuntamos una imagen de la deducción de las ecuaciones
    hit = False
    if b.y-20*value < p2.rect[1] + p2.rect[3] and b.y+20> p2.rect[1]: #coord x
        if b.x+10 > p2.rect[0] and b.x-10*value< p2.rect[0] + p2.rect[2]: #coord y
            hit = True
    return hit

def main():
    running = True
    n = Network()
    p = n.get_p()
    clock = pg.time.Clock()
        
    while running:
        
        clock.tick(FPS)
        p2 = n.send(p)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    b=p.shoot()
        for b in p.bullets:
            if p.y == 0:
                if hit(1,b,p2):
                    p.score += 1
                    b.kill()
            else:
                if hit(0,b,p2):
                    p.score += 1
                    b.kill()
        p.move()
        display(screen, p, p2)
        screen.blit(background, background_rect)
        
if __name__ == "__main__":
    main()
