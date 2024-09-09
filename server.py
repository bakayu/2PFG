import socket
from _thread import *
import pickle

try:
    with open('secret.pickle', 'rb') as reader:
        secret = pickle.load(reader)
except:
    pass

port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((secret, port))
except socket.error as e:
    print(e)

s.listen(2)
print("[SERVER STARTED] || Waiting for connection...")

players = [(110, 595, False, False, False, False, False, False, False, False, False, False, False, False, 400, False,
            False, False, False, False, 0),
           (1020, 595, False, False, False, False, False, False, False, False, False, False, False, False, 400, False,
           False, False, False, False, 1)]


def threaded_client(conn, player):
    global currentPlayer
    conn.send(pickle.dumps(players[player]))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("(Disconnected", addr)
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("received >> ", data)
                print("sending >> ", reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("(LOST Connection)")
    currentPlayer -= 1
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("(connected)", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
