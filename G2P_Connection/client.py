import pygame as pg
from network import Network

FPS = 60

WIDTH = 900
HEIGHT = 600

WHITE = (255,255,255)

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Caption")

        
def display(screen, player1, player2):
    screen.fill(WHITE)
    player1.draw(screen)
    player2.draw(screen)
    pg.display.update()
    
    for b in player1.bullets:
        b.draw(screen)
    for b in player2.bullets:
        b.draw(screen)
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
