import socket


class Server:

    def __init__(self, server_ip, port):

        self.socket = socket.socket()
        self.socket.bind((str(server_ip), int(port)))
        self.socket.listen(1)
        self.connection = None
        self.address = None
        self.bufer_size = 0
        self.json_data = 0

    def main(self):
        try:
            while 1:
                self.connection, self.address = self.socket.accept()

                # always setting up buffer size before a message
                self.bufer_size = self.connection.recv(8).decode('utf-8')

                if self.bufer_size.isdigit():
                    pass
                else:
                    self.connection.close()
                    continue

                data_recieve = self.connection.recv(int(self.bufer_size)).decode('utf-8')

                data_recieve = json.loads(data_recieve)

        except Exception as ex:
            print(ex)
        finally:
            self.socket.close()
