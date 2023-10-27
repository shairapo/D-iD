import cv2
import pygame
import threading
from moviepy.editor import VideoFileClip


from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

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
            # elif (received_value==2):
            #       print('video 2 is playing')
        

dispatcher = Dispatcher()
dispatcher.set_default_handler(default_handler)

server = BlockingOSCUDPServer(("192.168.1.65", 1337), dispatcher)
server.serve_forever()

def play_vid(animation_path):
    
    # cv2 windows setup ------------------------------------------------------

    # Open a video file or capture from a camera
    cap = cv2.VideoCapture(animation_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video files.")
        exit()

    # Create a window to display the video
    cv2.namedWindow('booking', cv2.WINDOW_NORMAL)
    # cv2.setWindowProperty('booking', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    # Get the screen's width and height
    screen_width = 600  # Set to your screen's width
    screen_height = 1024  # Set to your screen's height

    # Calculate the position for the 'shai' window to be full screen
    # cv2.moveWindow('shai', 1921, 0)
    # cv2.resizeWindow('booking', screen_width, screen_height)

    while True:
        # Read frames from both video files
        ret, frame = cap.read()

        # Check if frames were read successfully
        if not ret:
            print("Error reading frames.")
            break

        # Resize the frame to match the screen resolution
        # frame = cv2.resize(frame, (screen_width, screen_height))

        # Display the current frame
        cv2.imshow('booking', frame)


        # Check for user input to exit
        if cv2.waitKey() & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()
