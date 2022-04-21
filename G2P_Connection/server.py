import socket
import _thread as th
import sys
import pickle
from player import Player, Bullet

P_COLOR1 = (5,123,219)
P_COLOR2 =  (0,0,0)

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2)#max conections
print("Server started. Waiting for connection")

players = [Player(0,0,50,50,P_COLOR1), Player(0,550,50,50,P_COLOR2)]


def t_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                
            
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost connection")
    conn.close()

current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    th.start_new_thread(t_client, (conn, current_player))
    current_player += 1