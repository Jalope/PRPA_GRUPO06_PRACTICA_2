import socket
#import _thread as th
from multiprocessing import Process, Manager, Lock, current_process
import sys
import pickle
from game import Player, Bullet, Game

#IP del que haga de servidor
server = "127.0.0.1"
#Puerto por defecto
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen()
print("Server started. Waiting for connection")

games = {}
n_players = 0

def client(conn, addr, player, gameid):
    global n_players
    
    conn.send(pickle.dumps(games[gameid].players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            games[gameid].players[player] = data
            print (f"process: {current_process().player}")
            if gameid in games:
                game = games[gameid]
                if not data:
                    print("Disconnected")
                    break
                else:
                    if player == 1:
                        reply = games[gameid].players[0]
                    else:
                        reply = games[gameid].players[1]
            else:
                break                
            
            conn.sendall(pickle.dumps(reply))
        except:
            break
    
    print(f'Lost connection {addr}')
    try:
        del games[gameid]
        print(f'Deleted game {gameid}')
    except:
        pass
    n_players -= 1
    conn.close()

manager = Manager()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    n_players += 1
    n_game = (n_players-1)//2
    p = 0
    if n_players % 2 == 1:
        print(f'Creating game {n_game}')
        games[n_game] = Game(n_game)
    else:
        games[n_game].ready = True
        p = 1 
    new_player = Process(target = client, args = (conn, addr, p, n_game))
    new_player.start()
