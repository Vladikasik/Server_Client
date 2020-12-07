import socket

class CLient:

    def __init__(self, server_ip, port):

        self.request_data = request_data
        self.request_type = request_type
        self.sock1 = socket.socket()
        self.sock1.connect((str(server_ip), int(port)))
        self.buffer_size = 0

    def main(self, query):
        
