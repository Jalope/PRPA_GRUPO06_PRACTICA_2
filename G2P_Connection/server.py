import socket
import _thread as th
import sys
import pickle
from simpgame import Player



server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((server, port))
except socket.error as e:
	str(e)

s.listen(2)#max conections
print("Server started. Waiting for connection")


def t_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2408)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(replay))
        except:
            break
    print("Lost connection")
    conn.close()

current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    th.start_new_thread(t_client, (conn,))
    current_player += 1
