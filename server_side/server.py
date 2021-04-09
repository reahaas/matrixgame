import socket
from _thread import *
import pickle

from consts import server_address, server_port
from game_logic.game import Game


game_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    game_server.bind((server_address, server_port))
except socket.error as e:
    print(e)

game_server.listen(6)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0


def threaded_client(conn, player_id, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(4096))

            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data != "get":
                        game.action(player_id, data)

                    state = (game, player_id)
                    conn.sendall(pickle.dumps(state))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


current_player = 0
while True:
    conn, addr = game_server.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//7
    if idCount % 7 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")

    games[gameId].add_player(current_player)

    start_new_thread(threaded_client, (conn, current_player, gameId))
    current_player += 1
