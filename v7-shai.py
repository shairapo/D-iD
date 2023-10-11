import requests
import json
import time
import cv2
from PIL import Image
import os

# xxxxxtest


global video_name, voices, texts, textIndex

video_name=0

voices=["en-US-DavisNeural", "en-US-JennyNeural"]
texts= ["We didn't reach our steps goal for today, please go on walking",
        "Congratulations!!! We can rest now. Let's rest on the green spot",
        "Our blood pressure is soaring; why not meditate on the blue area in the corner?",
        "We are doing great! And our bank balance is fantastic, but unfortunately, our screen time is high above the average; please stop looking at the screens now.",
        "Please don't stand still; it's no good for digestion ",
        "Memories special for us are on the screen now",
        "It's our best 30-second walk! Congratulations!!!",
        "A daily hug is a prescription for good vibes. Today, we missed that embrace. Let's be kind to ourselves with a self-hug.",
        "Congratulations!!! It's our best hug; let's share it with a friend. "]


def capture_and_save_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam not found or could not be opened.")
        return
    
    image_path = "C:/Users/shai_/Desktop/github_Desktop/D-iD/image.jpeg"

     # Check if the original image exists and delete it
    if os.path.exists(image_path):
        os.remove(image_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture an image.")
            break

        small_frame = cv2.resize(frame, (1920, 1080))
        cv2.imshow("Press 'p' to take a photo", small_frame)

        key = cv2.waitKey(1)

        if key == ord('p' or 'P'):
            small_frame = cv2.resize(frame, (1920, 1080))
            cv2.imwrite(image_path, small_frame)
            print("Image captured and saved as 'image.jpeg'.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return image_path

def upload_image():
    url = "https://api.d-id.com/images"

    #this is the line that handles the uploading, currently only with the GUI on the website
    files = { "image": ("image.jpeg", open("image.jpeg", "rb"), "image/jpeg") }

    headers = {
        "accept": "application/json",
        # "content-type": "multipart/form-data",
        "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
    }

    response = requests.post(url, files=files, headers=headers)

    response_data = json.loads(response.text)

    # Extract and print the S3 URL
    s3_url = response_data.get("url")
    print("image url is:  " + s3_url)

    return s3_url


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
            print("video url is:  " + result_url)
            
    else:
        print("get_requests failed")
    
    return result_url


def download_video(url):
        
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.expanduser("C:/Users/shai_/Desktop/github_Desktop/D-iD/videos-shai")
        save_path = os.path.join(file_path, str(video_name)+ ".mp4")
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"Video downloaded and saved as {save_path}")
            
    else:
        print(f"Failed to download video. Status code: {response.status_code}")




def post_requests(text, image_url):

    url = "https://api.d-id.com/talks"

    payload = {
        "script": {
            "type": "text",
            "input": text,
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": voices[1],
                # "voice_config": {
                #     "style": "Whispering"
                # }
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
        time.sleep(10)
        download_video( get_requests(string) )
    else:
        print("id request failed")



# At the beginning, capture an image and get its path
image_path = capture_and_save_image()

# Upload the image and get the image URL
image_url = upload_image()

# # Perform the POST request with the image URL
# post_requests("Hello", image_url)


for x in range(9):
    post_requests(texts[video_name], image_url)
    video_name+=1
    print("next video will be named:  ", video_name)


if(video_name==9):
    print("all videos have been generated successfully")

