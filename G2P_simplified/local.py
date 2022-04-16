import random
import pygame



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 900
HEIGHT = 600

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

FPS = 60 

class Laser1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self): 
        self.rect.y -= 5 

class Laser2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self): 
        self.rect.y += 5 

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("meteor.png").convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player1.png").convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0

    #le pasamos el parametro x que representa la velocidad
    def changespeed(self, x): 
        self.speed_x += x
    
    #encapsulamos 
    def update(self): 
        self.rect.x += self.speed_x
        player1.rect.y = 510

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player2.png").convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()
        self.speed_x = 0
        self.speed_y = 0

    #le pasamos el parametro x que representa la velocidad
    def changespeed(self, x): 
        self.speed_x += x
    
    #encapsulamos 
    def update(self): 
        self.rect.x += self.speed_x
        palyer2.rect.y = 0


class Game(object):
    def __init__(self): 
        self.score_P1 = 0
        self.score_P2 = 0
        self.game_over = False
        self.all_sprite_list = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        self.laser_list1 = pygame.sprite.Group()
        self.laser_list2 = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()

        for i in range(50): 
            meteor = Meteor()
            meteor.rect.x = random.randrange(900 - 30)
            meteor.rect.y = random.randrange(450)

            self.meteor_list.add(meteor)
            self.all_sprite_list.add(meteor)

        self.player1 = Player1()
        self.player_list.add(self.player1)
        self.all_sprite_list.add(self.player1)

        self.player2 = Player2()        
        self.player_list.add(self.player2)
        self.all_sprite_list.add(self.player2)

    def process_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return False 

            if event.type == pygame.KEYDOWN:
                if self.game_over: 
                        self.__init__() 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player1.changespeed(-3)
                if event.key == pygame.K_RIGHT:
                    self.player1.changespeed(3)

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT:
                    self.player1.changespeed(3)
                if event.key == pygame.K_RIGHT:
                    self.player1.changespeed(-3)

        #cada vez que pulso sale un laser 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    laser = Laser1()
                    laser.rect.x = self.player1.rect.x + 45
                    laser.rect.y = self.player1.rect.y - 20
                
                    self.laser_list1.add(laser)
                    self.all_sprite_list.add(laser)
                
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_SPACE:
                    pass 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player2.changespeed(-3)
                if event.key == pygame.K_d:
                    self.player2.changespeed(3)

            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_a:
                    self.player2.changespeed(3)
                if event.key == pygame.K_d:
                    self.player2.changespeed(-3)

        #cada vez que pulso sale un laser 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w: 
                    laser = Laser2()
                    laser.rect.x = self.player2.rect.x + 45
                    laser.rect.y = self.player2.rect.y + 65
                
                    self.laser_list2.add(laser)
                    self.all_sprite_list.add(laser)
                
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_w:
                    pass 
        
        return True
    
    def run_logic(self): 
        if not self.game_over: 
            self.all_sprite_list.update()

        for laser in self.laser_list1: 
            meteor_hit_list = pygame.sprite.spritecollide(laser, self.meteor_list, True)
            for meteor in meteor_hit_list: 
                self.all_sprite_list.remove(laser)
                self.laser_list1.remove(laser)
                #score +=1 
                #print(score)
        
            if laser.rect.y < -10: 
                self.all_sprite_list.remove(laser)
                self.laser_list1.remove(laser)
    
        for laser in self.laser_list2: 
            meteor_hit_list = pygame.sprite.spritecollide(laser, self.meteor_list, True)
            for meteor in meteor_hit_list: 
                self.all_sprite_list.remove(laser)
                self.laser_list2.remove(laser)
                score +=1 
                print(score)
        
            if laser.rect.y < -10: 
                self.all_sprite_list.remove(laser)
                self.laser_list2.remove(laser)

        for laser in self.laser_list1: 
            if pygame.sprite.collide_rect(laser, self.player2):
                self.all_sprite_list.remove(self.player2)
                self.laser_list1.remove(laser)
        
            if laser.rect.y < -10: 
                self.all_sprite_list.remove(laser)
                self.laser_list1.remove(laser)

        for laser in self.laser_list2: 
            if pygame.sprite.collide_rect(laser, self.player1):
                self.all_sprite_list.remove(self.player1)
                self.laser_list2.remove(laser)
         
            if laser.rect.y < -10: 
                self.all_sprite_list.remove(laser)
                self.laser_list2.remove(laser)

    def display_frame(self, screen): 
        screen.fill(WHITE)

         #texto para game over 
        if self.game_over: 
            font = pygame.font.SysFont("serif", 25) #Fuente
            text = font.render("Game Over! Click to continue", True, BLACK) #Texto 
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) #posicion del texto
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y]) #imprimirlo en la ventana del juego
        else: 
            self.all_sprite_list.draw(screen)

        self.all_sprite_list.draw(screen)
        pygame.display.flip()

def main(): 

    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()
    running = True 
    
    game = Game()

    while running: 
        running = game.process_events()
        game.run_logic
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__": 
    main()
