# the problem here is that moviepy can't be allocated to a display, seems to not have this feature 

from moviepy.editor import VideoFileClip
from screeninfo import get_monitors

# Function to list all available displays
def list_displays():
    screens = get_monitors()
    return screens

if __name__ == "__main__":
    # List available displays
    displays = list_displays()

    if not displays:
        print("No displays found.")
    else:
        print("Available Displays:")
        for i, display in enumerate(displays):
            print(f"Display {i}: {display.width}, {display.height}")

        # Choose a display to play the video on (e.g., Display 1)
        display_index = 1  # Change this to the index of the desired display

        if display_index >= len(displays):
            print(f"Invalid display index {display_index}")
        else:
            # Path to the video file
            video_path = "videos-shai/1.mp4"  # Replace with the actual video file path

            try:
                # Load the video
                video_clip = VideoFileClip(video_path)

                # Get the chosen display
                target_display = displays[display_index]

                # Create a window with the chosen display resolution
                video_clip.preview(fps=30)  # Adjust the fps as needed

            except Exception as e:
                print(f"Error: {e}")
