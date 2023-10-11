import pyautogui
import keyboard

def print_mouse_position():
    x, y = pyautogui.position()
    print(f"Mouse position: X = {x}, Y = {y}")

print("Press 'l' to print mouse position when released, long 'esc' to stop...")

# Initialize a variable to track if 'l' is currently pressed
l_pressed = False

while True:
   
    # Check if 'esc' key is pressed to exit
    if keyboard.is_pressed('esc'):
        break
    
    # Check if 'l' key is pressed
    if keyboard.is_pressed('l'):
        if not l_pressed:
            l_pressed = True
            print_mouse_position()
    else:
        l_pressed = False

keyboard.wait('esc')  # Wait for the 'esc' key press to exit
