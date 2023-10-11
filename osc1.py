from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from typing import List, Any

def default_handler(address, *args):
    
    if args:
            received_value = args[0]
            print(f"received: {received_value}")
    # print(f"received: {address}: {args}")
    # print(f"received: {args}")

dispatcher = Dispatcher()
dispatcher.set_default_handler(default_handler)

server = BlockingOSCUDPServer(("192.168.1.65", 1337), dispatcher)
server.serve_forever()