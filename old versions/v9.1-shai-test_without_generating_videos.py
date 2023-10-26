# This is an isolated version of v9-shai.py, without a second vid and without all the irrelvant code for the test
# In this code we are testing the triggering of videos according to the openframeworks code. process of creating the videos was taken out. 
# it seems like this code is working ok, need some more critical examination


import requests
import json
import time
import cv2
from PIL import Image
import os

# playing the videos imports
import pygame
import threading
from moviepy.editor import VideoFileClip

# osc
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from typing import List, Any
import random


video_name=0


# video names to pick from according to speeds
none=[0,1]
slow=[2,3,4]
medium=[5,6]
fast=[7,8]


def play_vids(d_id_vid):

    cap2 = cv2.VideoCapture(d_id_vid)

    # Check if the video file was opened successfully
    if not cap2.isOpened():
        print("Error: Could not open video files.")
        exit()

    # Create a window to display the video
    cv2.namedWindow('shai', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('shai', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Audio setup -----------------------

    # Function to play the audio using Pygame
    def play_audio(audio_clip):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_clip)
        pygame.mixer.music.play()

    # Load the video clip
    video_clip = VideoFileClip(d_id_vid)

    # Get the frame rate of the video
    frame_rate = video_clip.fps

    # Extract the audio from the video
    audio_clip_path = "temp_audio.wav"  # Temporary audio file path
    video_clip.audio.write_audiofile(audio_clip_path, codec="pcm_s16le")

    # Create and start a thread to play audio
    audio_thread = threading.Thread(target=play_audio, args=(audio_clip_path,))
    audio_thread.daemon = True
    audio_thread.start()

    # Get the screen's width and height
    screen_width = 1080  # Set to your screen's width
    screen_height = 1920  # Set to your screen's height

    # Calculate the position for the 'shai' window to be full screen
    cv2.resizeWindow('shai', screen_width, screen_height)

    while True:
        # Read frames from both video files
        ret2, frame2 = cap2.read()

        # Check if frames were read successfully
        if not ret2:
            print("Error reading frames.")
            break

        # Resize the frame to match the screen resolution
        frame2 = cv2.resize(frame2, (screen_width, screen_height))

        # Display the current frame
        cv2.imshow('shai', frame2)

        # Check for user input to exit
        if cv2.waitKey(int(800 / frame_rate)) & 0xFF == ord('q'):
            break

    
    # Release the video capture object and close all windows
    cap2.release()
    pygame.mixer.quit()
    cv2.destroyAllWindows()
    playback_finished_event.set()
    

if(video_name == 0):
    print("all videos have been generated successfully, starting the listening to messages")

    playback_finished_event = threading.Event()

    def default_handler(address, *args):
        if args:
                received_value = args[0]
                # print(f"received: {received_value}")
                # print(f"received: {address}: {args}")
                # print(f"received: {args}")

                if (received_value == 0):
                    index = random.randint(0, 1)
                    d_id_vid='videos-shai/' + str(none[index]) + '.mp4'
                    print("playing video number: "+str(none[index]))
                    play_vids(d_id_vid)
                    playback_finished_event.wait()
                elif (received_value == 1):
                    index = random.randint(0, 2)
                    d_id_vid='videos-shai/' + str(slow[index]) + '.mp4'
                    print("playing video number: "+str(slow[index]))
                    play_vids(d_id_vid)
                    playback_finished_event.wait()
                elif (received_value == 2):
                    index = random.randint(0, 1)
                    d_id_vid='videos-shai/' + str(medium[index]) + '.mp4'
                    print("playing video number: "+str(medium[index]))
                    play_vids(d_id_vid)
                    playback_finished_event.wait()
                elif (received_value == 3):
                    index = random.randint(0, 2)
                    d_id_vid='videos-shai/' + str(fast[index]) + '.mp4'
                    print("playing video number: "+str(fast[index]))
                    play_vids(d_id_vid)
                    playback_finished_event.wait()

    dispatcher = Dispatcher()
    dispatcher.set_default_handler(default_handler)

    server = BlockingOSCUDPServer(("192.168.1.65", 1337), dispatcher)
    server.serve_forever()
    
    
    

