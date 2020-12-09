import socket
import json
from Server.database import Database
import rsa


class Server:

    def __init__(self, server_ip, port):

        self.socket = socket.socket()
        self.socket.bind((str(server_ip), int(port)))
        self.socket.listen(1)
        self.db = Database()
        self.connection = None
        self.address = None
        self.bufer_size = 0
        self.json_data = 0

        (self.my_pubkey, self.privkey) = rsa.newkeys(2048)

    def start(self):
        print('запустился сервер')
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

                query_type = data_recieve["Type"]
                if query_type == "PubKey":
                    self.db.write_new_id(data_recieve["Message"]["Id"], data_recieve["Message"]["PubKey"], self.my_pubkey, self.privkey)
                elif query_type == "Message":
                    if self.db.user_exists(data_recieve):
                        print('Message from registrated user -', data_recieve["Message"]["Id"])
                        privKey = self.db.get_privkey(data_recieve)

                print(data_recieve)
                print('recieved')

        except Exception as ex:
            print(ex)
        finally:
            self.socket.close()
