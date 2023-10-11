#same thing as previous version but with some chatgpt corrections

import cv2
import pygame
import threading
from moviepy.editor import VideoFileClip

# Define the file paths for the two video files
video_file1 = 'small_anim.mp4'
video_file2 = 'videos-shai/1.mp4'

# cv2 windows setup ------------------------------------------------------

# Open a video file or capture from a camera
cap1 = cv2.VideoCapture(video_file1)
cap2 = cv2.VideoCapture(video_file2)

# Check if the video file was opened successfully
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video files.")
    exit()

# Create a window to display the video
cv2.namedWindow('underwater', cv2.WINDOW_NORMAL)
cv2.namedWindow('shai', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('shai', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Audio setup -----------------------

# Function to play the audio using Pygame
def play_audio(audio_clip):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_clip)
    pygame.mixer.music.play()

# Load the video clip
video_clip = VideoFileClip(video_file2)

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
cv2.moveWindow('shai', 1921, 0)
cv2.moveWindow('underwater', 300, 200)
cv2.resizeWindow('shai', screen_width, screen_height)

while True:
    # Read frames from both video files
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Check if frames were read successfully
    if not ret1 or not ret2:
        print("Error reading frames.")
        break

    # Resize the frame to match the screen resolution
    frame2 = cv2.resize(frame2, (screen_width, screen_height))

    # Display the current frame
    cv2.imshow('underwater', frame1)
    cv2.imshow('shai', frame2)

    # Check for user input to exit
    if cv2.waitKey(int(800 / frame_rate)) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()
