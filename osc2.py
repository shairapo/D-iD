from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
# from typing import List, Any
import random

none=[0,1]
slow=[2,3,4]
medium=[5,6]
fast=[7,8,9]


def default_handler(address, *args):
    if args:
            received_value = args[0]
            # print(f"received: {received_value}")
            # print(f"received: {address}: {args}")
            # print(f"received: {args}")
            if (received_value==0):
                  rand_num = random.randint(0, 1)
                  print(none[rand_num])
            elif (received_value==1):
                  rand_num = random.randint(0, 2)
                  print(slow[rand_num])
            elif (received_value==2):
                  rand_num = random.randint(0, 1)
                  print(medium[rand_num])
            elif (received_value==3):
                  rand_num = random.randint(0, 2)
                  print(fast[rand_num])

dispatcher = Dispatcher()
dispatcher.set_default_handler(default_handler)

server = BlockingOSCUDPServer(("192.168.1.65", 1337), dispatcher)
server.serve_forever()


