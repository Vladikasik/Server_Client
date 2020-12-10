import socket
import rsa
from Client.client_queries import msg

class CLient:

    def __init__(self, server_ip, port, id):

        self.sock = socket.socket()
        self.sock.connect((str(server_ip), int(port)))
        self.buffer_size = 0

        (self.pubkey, self.privkey) = rsa.newkeys(2048)

        self.id = id

    def send(self, query):

        if query == 'PubKey':
            data = [self.pubkey.save_pkcs1().decode(), self.id]
            data_to_send = msg(query, data)
            self.sock.send(str(len(data_to_send)).encode())
            self.sock.send(data_to_send)

        print(data_to_send)
        print('sent')
