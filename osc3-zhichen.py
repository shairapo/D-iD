from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

address = "192.168.1.100"
port = 8888

def gender_generation(address, *args):
    generation = args[0]
    if generation == 1 :
        print(f"Received OSC message for {address}: " + f"{generation}")

def gender_handler(address, *args):
    gender = args[0]
    # print(f"Received OSC message for {address}: " + f"{gender}")

def style_handler(address, *args):
    style = args[0]
    # print(f"Received OSC message for {address}: " + f"{style}")

dispatcher = Dispatcher()
dispatcher.map("/generation", gender_generation)
dispatcher.map("/gender", gender_handler)
dispatcher.map("/style",  style_handler)

server = osc_server.ThreadingOSCUDPServer((address, port), dispatcher)
server.serve_forever()