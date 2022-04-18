import pygame as pg
from network import Network


width = 900
height = 600
win = pg.display.set_mode((width,height))
pg.display.set_caption("Caption")

        
def display(win, player1, player2):
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)
     
    for b in player1.bullets:
        b.draw(win)
    for b in player2.bullets:
        b.draw(win)
    pg.display.update()

def main():
    running = True
    n = Network()
    p = n.get_p()
    clock = pg.time.Clock()
    
    while running:
        all_sprites = pg.sprite.Group()       
        clock.tick(60)
        p2 = n.send(p)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    b=p.shoot()
                    all_sprites.add(b)
        p.move()
        all_sprites.update()           
        display(win, p, p2)
        
if __name__ == "__main__":
    main()