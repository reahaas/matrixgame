import socket
import pickle

from consts import server_address, server_port


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server_address
        self.port = server_port
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

