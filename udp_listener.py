import socket
import os

PORT = os.getenv("PORT", 5005)

direction_lookup = {
    0: 'left',
    1: 'straight',
    2: 'right'
}

class Listener:
    def __init__(self, callback):
        self.callback = callback
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', PORT))

    def listen(self):
        while True:
            data, _ = self.sock.recvfrom(1024)
            data = data.decode('utf-8')
            servo = data[:2]
            direction = direction_lookup[int(data[2])]
            self.callback(servo, direction)