#the file path need to be changed in line 44, 65, 247


import requests
import json
import time
import cv2
from PIL import Image
import os

from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

import subprocess

address = "192.168.1.65"
port    = 8888

vidDone = None

def voice_gender(gender):
    if(gender == 1): 
        return "en-US-DavisNeural"
    if(gender == 2): 
        return "en-US-BlueNeural"
    if(gender == 3): 
        return "en-US-AriaNeural"
    
def voice_style(style):
    if(style == 1): 
        return "Friendly"
    if(style == 2): 
        return "Sad"
    if(style == 3): 
        return "Cheerful"
    if(style == 4): 
        return "Whispering"
    if(style == 5): 
        return "Shouting"
    
    
# **************************************** #
# **************************************** #
def save_image():
    
    image_path = "C:/Users/shai_/Desktop/github_Desktop/D-iD/image.jpeg"
    return image_path

def download_video(url, save_path, vidDone):
        
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"Video downloaded and saved as {save_path}")
            
            vidDone += 1
            print(f"Video Done {vidDone} ")
            # runOpenframeworks(vidDone)

    else:
        print(f"Failed to download video. Status code: {response.status_code}")

file_path = os.path.expanduser("C:/Users/shai_/Desktop/github_Desktop/D-iD/videos-shai/")

save_path_0 = os.path.join(file_path, "0.mp4")
save_path_1 = os.path.join(file_path, "1.mp4")
save_path_2 = os.path.join(file_path, "2.mp4")
save_path_3 = os.path.join(file_path, "3.mp4")
save_path_4 = os.path.join(file_path, "4.mp4")
save_path_5 = os.path.join(file_path, "5.mp4")
save_path_6 = os.path.join(file_path, "6.mp4")
save_path_7 = os.path.join(file_path, "7.mp4")
save_path_8 = os.path.join(file_path, "8.mp4")
save_path_9 = os.path.join(file_path, "9.mp4")


def get_requests(string):

    url = f"https://api.d-id.com/talks/{string}"
    headers = {
        "accept": "application/json",
        "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
    }

    response = requests.get(url, headers=headers)
    # print(response.text)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "done":
            result_url = data["result_url"]
            # print(result_url)
    else:
        print("get_requests failed")
    
    return result_url


def upload_image():
    url = "https://api.d-id.com/images"

    #this is the line that handles the uploading, currently only with the GUI on the website
    files = { "image": ("image.jpeg", open("image.jpeg", "rb"), "image/jpeg") }

    headers = {
        "accept": "application/json",
        "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
    }

    response = requests.post(url, files=files, headers=headers)

    response_data = json.loads(response.text)

    # Extract and print the S3 URL
    s3_url = response_data.get("url")
    print(s3_url)
    return s3_url


# **************************************** #
# **************************************** #
def post_requests_mAndf(text, image_url, gender, style, save_path, vidDone):

    url = "https://api.d-id.com/talks"

    payload = { 
        "script": {
            "type": "text",
            "input": text,
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": voice_gender(gender),
                "voice_config": {
                    "style": voice_style(style)
                }
            },
            "ssml": "false"
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        
        "webhook": "https://host.domain.tld/to/webhook",
        "source_url": image_url

    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
    }

    response = requests.post(url, json=payload, headers=headers)
    # print(response.text)

    if response.status_code == 201:
        data = response.json()
        # print (data["id"])
        string = data["id"]

        # Wait for the image uploading to the platform
        time.sleep(5)
        download_video( get_requests(string), save_path, vidDone)
    else:
        print("id request failed")


def post_requests_noneB(text, image_url, gender, save_path, vidDone):

    url = "https://api.d-id.com/talks"

    payload = { 
        "script": {
            "type": "text",
            "input": text,
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": voice_gender(gender),
            },
            "ssml": "false"
        },
        "config": {
            "fluent": "false",
            "pad_audio": "0.0"
        },
        
        "webhook": "https://host.domain.tld/to/webhook",
        "source_url": image_url

    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
    }

    response = requests.post(url, json=payload, headers=headers)
    # print(response.text)

    if response.status_code == 201:
        data = response.json()
        # print (data["id"])
        string = data["id"]

        # Wait for the image uploading to the platform
        time.sleep(5)
        download_video( get_requests(string), save_path, vidDone)
    else:
        print("id request failed")


# **************************************** #
# **************************************** #
def gender_generation(address, *args):
    generation = args[0]
    gender     = args[1]
    style      = args[2]
    if generation == 1  and gender != 3:

        global vidDone
        vidDone = 0
        print(f"Video Done {vidDone} ")

        # subprocess.call(["pkill", "-f", "Gui_playVidDebug.app"])

        image_url = upload_image()

        # stand
        post_requests_mAndf("Oh, look, it’s Google’s “Memories Together”! Great photos. What an awesome vacation it was. We haven’t booked one for more than six months. We see a hotel rated ‘superb’ 9.2 by 752 reviewers, 200 yards from the beach. No breakfast included. Lowest price in 30 days. Booked! Congratulations! Confetti ball!", image_url, gender, style, save_path_0, vidDone)
        post_requests_mAndf("Hurray! It’s our best 10-second meditation! We have earned 1,250 coins. It's time for a walk. We should try to reach our daily step count. Start walking.", image_url, gender, style, save_path_1, vidDone)
        post_requests_mAndf("Please don't stand still; it's not good for our digestion. We love walking.", image_url, gender, style, save_path_2, vidDone)
        # medium
        post_requests_mAndf("We’re on fire! It’s our best gallery walk! Keep walking and have a positive mindset. We are heading towards our daily step-count goal.", image_url, gender, style, save_path_3, vidDone)
        post_requests_mAndf("Our third favourite cousin started a new job at Tesla. Would we like to congratulate them? We’re so fucking proud of them and green with envy. Clap your hands.", image_url, gender, style, save_path_4, vidDone)
        post_requests_mAndf("Bravo! Clap your hands! Clap your hands!", image_url, gender, style, save_path_5, vidDone)
        post_requests_mAndf("We are the second-best visitor today! We are rated 4.7! Confetti! Red heart! Clapping hands!", image_url, gender, style, save_path_6, vidDone)
        # high
        post_requests_mAndf("Our pulse is too fast. Our sleep quality is below average. We should reduce stress. Sit down in the corner and practice meditation. You’ve got this!", image_url, gender, style, save_path_7, vidDone)
        post_requests_mAndf("We have earned 3,534 coins. Well done!", image_url, gender, style, save_path_8, vidDone)
        post_requests_mAndf("We are doing great! Our bank balance is fantastic. Unfortunately, our screen time is well above average; please stop looking at the screens for a while.", image_url, gender, style, save_path_9, vidDone)
        
        
        
    
    # if generation == 1  and gender == 3:
    #     None       
        # can not be used caz lack of the library   

        # image_url = upload_image()
        # post_requests_noneB("Hello nice to meet you!", image_url, gender, save_path_0, vidDone) 


def runOpenframeworks(vidDone):
    app_path = "/Users/zhichengu/Desktop/Gui_playVidDebug.app"

    if vidDone == 1:
        subprocess.Popen(["open", app_path])


# **************************************** #
# **************************************** #
image_path = save_image()

dispatcher = Dispatcher()
dispatcher.map("/generation", gender_generation)

server = osc_server.ThreadingOSCUDPServer((address, port), dispatcher)
server.serve_forever()

