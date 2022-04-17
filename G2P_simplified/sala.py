from multiprocessing.connection import Listener
from multiprocessing import Process, Manager, Value, Lock 
import traceback
import sys
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SIDESSTR = ['up', 'down']

WIDTH = 900
HEIGHT = 600

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

UP_PLAYER = 510
DOWN_PLAYER = 0

FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, side, imagE):
        super().__init__()
        self.side = side
        self.image = pygame.image.load(imagE).convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect() #(x,y)
        self.speed_x = 0
        self.speed_y = 0

    def get_rect(self): 
        return self.rect 
    
    def get_side(self): 
        return self.side 
    
    #le pasamos el parametro x que representa la velocidad
    def changespeed(self, x): 
        self.speed_x += x
    
    #encapsulamos 
    def update(self): 
        self.rect.x += self.speed_x
        self.rect.y = self.side


class Game(object):
    def __init__(self, manager): 
        #self.score_P1 = Value('i', 0) 
        #self.score_P2 = Value('i', 0)
        self.score = manager.list([0, 0])
        self.game_over = Value('i', 0) #0 -> False
        self.all_sprite_list = pygame.sprite.Group()
        self.meteor_list = pygame.sprite.Group()
        self.laser_list1 = pygame.sprite.Group()
        self.laser_list2 = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()
        self.win_player = Value('i', 0)
  
        self.player1 = Player(510, "player1.png")
        self.player_list.add(self.player1)
        self.all_sprite_list.add(self.player1)

        self.player2 = Player(0, "player2.png")        
        self.player_list.add(self.player2)
        self.all_sprite_list.add(self.player2)

        self.players = manager.list([self.player1, self.player2])

        self.lock = Lock()
    
    def get_player(self, side): 
        return self.players[side]

    def update_PRUEBA(self, player): 
        self.lock.acquire()
        p = self.players[player]
        p.update()
        self.players[player] = p 
        self.lock.release()
    
    def get_score(self):
        return list(self.score)

    def is_running(self): 
        return self.game_over.value == 0
    
    def stop(self): 
        self.game_over = 1
    

    


    def get_info(self): 
        info = { 'pos_up_player' : self.players[UP_PLAYER].get_pos(), 
                'pos_down_player' : self.players[DOWN_PLAYER].get_pos(),
                'score' : list(self.score), 
                'is_running' : (self.game_over.value == 1) }
        return info 

def player(side, conn, game): 
    try: 
        print(f"starting player {SIDESSTR[side]}:{game.get_info()}")
        conn.send((side, game.get_info()))
        while game.is_running(): 
            command = "" 
            while command != "next": 
                command = conn.recv()
                if command == "up": 
                    game.update_PRUEBA(side)
                elif command == "down": 
                    game.update_PRUEBA(side)
                elif command == "quit": 
                    game.stop()
            conn.send(game.get_info())
    except: 
        traceback.print_exc()
        conn.close()
    finally: 
        print(f"Game ended {game}")

def main(ip_address):
    #screen = pygame.display.set_mode([WIDTH, HEIGHT])
    manager = Manager()
    try:
        with Listener((ip_address, 6000),
                      authkey=b'secret password') as listener:
            n_player = 0
            players = [None, None]
            game = Game(manager)
            while True:
                print(f"accepting connection {n_player}")
                conn = listener.accept()
                players[n_player] = Process(target=player,
                                            args=(n_player, conn, game))
                n_player += 1
                if n_player == 2:
                    players[0].start()
                    players[1].start()
                    n_player = 0
                    players = [None, None]
                    game = Game(manager)

    except Exception as e:
        traceback.print_exc()

if __name__=='__main__':
    ip_address = "127.0.0.1"
    if len(sys.argv)>1:
        ip_address = sys.argv[1]

    main(ip_address)