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

    while True:
        ret, frame = cap.read()

        if not ret:
            print("End of video.")
            break

        cv2.imshow('booking', frame)

        key = cv2.waitKey(delay)  # Adjust delay to control playback speed

        if key & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    playback_finished_event.set()



def default_handler(address, *args):
    if args:
            received_value = args[0]
            # print(f"received: {received_value}")
            # print(f"received: {address}: {args}")
            # print(f"received: {args}")
            if (received_value==1):
                  print('video 1 is playing')
                  animation_path='videos-shai/' + str(received_value) + '.mp4'
                  play_vid(animation_path)
                  playback_finished_event.wait()
            # elif (received_value==2):
            #       print('video 2 is playing')
        

playback_finished_event = threading.Event()

dispatcher = Dispatcher()
dispatcher.map("/mini",default_handler)
# dispatcher.set_default_handler(default_handler)

server = BlockingOSCUDPServer(("192.168.1.188", 1337), dispatcher)
server.serve_forever()



