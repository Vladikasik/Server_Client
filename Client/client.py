import socket
import rsa
from Client.client_queries import msg


class CLient:

    def __init__(self, server_ip, port, id):
        self.sock = socket.socket()
        self.sock.connect((str(server_ip), int(port)))
        self.buffer_size = 0

        (self.my_pubkey, self.privkey) = rsa.newkeys(2048)

        self.id = id

    def send(self, query, data):
        data_to_send = {"Type": "Error", "Message": "We are working on it"}

        if query == 'PubKey':
            data_keys = [self.my_pubkey.save_pkcs1().decode(), self.id]
            data_to_send = msg(query, data_keys)
            self.sock.send(str(len(data_to_send)).encode())
            self.sock.send(data_to_send)
        if query == 'Message':
            data_msg = [self.id, data, self.my_pubkey]
            data_to_send = msg(query, data_msg)
            self.sock.send(str(len(data_to_send)).encode())
            self.sock.send(data_to_send)

        print(data_to_send)
        print('sent')
