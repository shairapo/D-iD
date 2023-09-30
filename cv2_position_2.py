import cv2

# Open a video file or capture from a camera
cap = cv2.VideoCapture("videos-shai/1.mp4")  # Replace "your-video.mp4" with your video file path

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
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
