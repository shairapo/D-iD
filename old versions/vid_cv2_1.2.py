# play 2 videos, one in full screen, no sound, in a specific position on screens/monitors

import cv2

# Define the file paths for the two video files
video_file1 = 'small_anim.mp4'
video_file2 = 'videos-shai/1.mp4'

# Open a video file or capture from a camera
cap1 = cv2.VideoCapture(video_file1) 
cap2 = cv2.VideoCapture(video_file2)

# Check if the video file was opened successfully
if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video files.")
    exit()

# Create a window to display the video
cv2.namedWindow('underwater', cv2.WND_PROP_FULLSCREEN)
cv2.namedWindow('shai', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('underwater', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


# Move the window to the desired position
cv2.moveWindow('underwater', 1920, 0)
cv2.moveWindow('shai', 200, 300)

while True:

    # Read frames from both video files
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

   # Check if frames were read successfully
    if not ret1 or not ret2:
        print("Error reading frames.")
        break

    # Display the current frame
    cv2.imshow('underwater', frame1)
    cv2.imshow('shai', frame2)

    # Check for user input to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()
