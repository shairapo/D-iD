from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

address = "192.168.1.100"
port = 8888

gender = None

# Define a callback function to handle received OSC messages
def gender_handler(address, *args):
    global gender
    gender = args[0]
    print(f"Received OSC message for {address}: " + f"{gender}")

def style_handler(address, *args):
    global style
    style = args[0]
    print(f"Received OSC message for {address}: " + f"{style}")

# Create an OSC dispatcher and associate the handlers with specific addresses
dispatcher = Dispatcher()
dispatcher.map("/gender", gender_handler)
dispatcher.map("/style",  style_handler)

# Create an OSC server to listen for incoming OSC messages
server = osc_server.ThreadingOSCUDPServer((address, port), dispatcher)
server.serve_forever()


# Function to print the gender
def numberGender():
    global gender
    print("Current gender:", gender)

# Call the numberGender function to print the gender
numberGender()