from threading import Thread

import time

from Server.server import Server
from Client.client import CLient

ser = Server('localhost', 7778)
server = Thread(target=ser.start)
server.start()

cli = CLient('localhost', 7778, 12316)
client = Thread(target=cli.send, args=('PubKey',))
client.start()
