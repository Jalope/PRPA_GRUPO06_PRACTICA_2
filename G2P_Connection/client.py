import pygame as pg
from network import Network

FPS = 60

WIDTH = 900
HEIGHT = 600

WHITE = (255,255,255)

pg.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Caption")

font_name = pg.font.match_font('arial')
def draw_text(surf, text, size, x, y):
	font = pg.font.Font(font_name, size)
	text_surface = font.render(text, True, (0,0,0))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)


def display(screen, player1, player2):
    screen.fill(WHITE)
    player1.draw(screen)
    player2.draw(screen)
	draw_text(screen, f'score: ({player2.score},{player1.score})', width/2, height/2)
    pg.display.update()
    
def main():
    running = True
    n = Network()
    p = n.get_p()
    clock = pg.time.Clock()
    
    while running:
        
        #all_sprites = pg.sprite.Group()       
        clock.tick(FPS)
        p2 = n.send(p)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    b=p.shoot()
                    #all_sprites.add(b)
        p.move()
        #all_sprites.update()
        
        
        display(screen, p, p2)
        
if __name__ == "__main__":
    main()
