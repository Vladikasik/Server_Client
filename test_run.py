from threading import Thread

import time

from Server.server import Server
from Client.client import CLient

ser = Server('localhost', 7777)
server = Thread(target=ser.start)
server.start()

cli = CLient('localhost', 7777, 12316)
# client = Thread(target=cli.send, args=('PubKey', None,))
# client.start()
time.sleep(3)
client = Thread(target=cli.send, args=('Message', "Hello",))
client.start()
