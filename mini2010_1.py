import cv2
import threading
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

# Define a flag to indicate whether the video is currently playing
video_playing = False

def play_vid(animation_path):
    global video_playing

    # Set the flag to True to indicate that video playback has started
    video_playing = True

    # Open a video file
    cap = cv2.VideoCapture(animation_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        video_playing = False  # Set the flag to False
        return

    # Create a window to display the video
    cv2.namedWindow('booking', cv2.WINDOW_NORMAL)

    while True:
        # Read frames from the video file
        ret, frame = cap.read()

        # Check if frames were read successfully
        if not ret:
            print("Video playback finished.")
            break

        # Display the current frame
        cv2.imshow('booking', frame)

        # Check for user input to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

    # Set the flag to False when video playback is finished
    video_playing = False

def default_handler(address, *args):
    global video_playing

    if args:
        received_value = args[0]

        if received_value == 1:
            # Check if video is already playing
            if not video_playing:
                print('Video 1 is playing')
                animation_path = 'videos-shai/' + str(received_value) + '.mp4'
                # Create and start a new thread to play the video
                threading.Thread(target=play_vid, args=(animation_path,)).start()

dispatcher = Dispatcher()
dispatcher.map("/mini", default_handler)

server = BlockingOSCUDPServer(("192.168.1.188", 1337), dispatcher)
server.serve_forever()
