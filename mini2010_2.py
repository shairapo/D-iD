import cv2
import pygame
import threading
from moviepy.editor import VideoFileClip

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

def play_vid(animation_path, delay=30):
    cap = cv2.VideoCapture(animation_path)
    
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get the screen dimensions
    screen_width = 1024  # Adjust to your screen resolution
    screen_height = 600  # Adjust to your screen resolution

    # Create a full-screen window
    cv2.namedWindow('animation', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('animation', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video.")
            break

        # Resize the frame to match the screen dimensions
        frame = cv2.resize(frame, (screen_width, screen_height))

        cv2.imshow('animation', frame)

        key = cv2.waitKey(delay)  # Adjust delay to control playback speed

        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    playback_finished_event.set()

def default_handler(address, *args):
    if args:
        print('Value received')
        received_value = args[0]
        animation_path = 'animations/' + str(received_value) + '.mp4'
        play_vid(animation_path)
        playback_finished_event.wait()

playback_finished_event = threading.Event()

dispatcher = Dispatcher()
dispatcher.map("/mini", default_handler)

server = BlockingOSCUDPServer(("10.254.100.27", 1337), dispatcher)
server.serve_forever()
