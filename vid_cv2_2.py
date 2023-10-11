# this code plays a mute video in cv2 at the same time as playing the audio with pygame

# change this to position the video differently:
# cv2.moveWindow("Video", 1900, 0)

# change this to match the sync better:
# int(940 / frame_rate)

import cv2
import pygame
import threading
from moviepy.editor import VideoFileClip

# Video file path
video_path = 'videos-shai/1.mp4'  # Replace with your video file path

# Function to play the audio using Pygame
def play_audio(audio_clip):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_clip)
    pygame.mixer.music.play()

# Load the video clip
video_clip = VideoFileClip(video_path)

# Get the frame rate of the video
frame_rate = video_clip.fps

# Open a video file or capture from a camera
cap = cv2.VideoCapture(video_path)  # Replace "your-video.mp4" with your video file path

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get the screen's width and height
screen_width = int(cap.get(3))
screen_height = int(cap.get(4))

# Create a window to display the video
cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
cv2.moveWindow("Video", 1900, 0)
cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Extract the audio from the video
audio_clip_path = "temp_audio.wav"  # Temporary audio file path
video_clip.audio.write_audiofile(audio_clip_path, codec="pcm_s16le")

# Create and start a thread to play audio
audio_thread = threading.Thread(target=play_audio, args=(audio_clip_path,))
audio_thread.daemon = True
audio_thread.start()

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the video has ended
    if not ret:
        break

    # Resize the frame to match the screen resolution
    frame = cv2.resize(frame, (screen_width, screen_height))

    # Display the current frame
    cv2.imshow("Video", frame)

    # Check for user input to exit
    if cv2.waitKey(int(940 / frame_rate)) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
