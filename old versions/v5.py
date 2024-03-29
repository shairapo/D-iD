import requests
import json
import time
import cv2
from PIL import Image
import os


def capture_and_save_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Webcam not found or could not be opened.")
        return
    
    image_path = "/Users/zhichengu/Documents/GitHub/D-iD/image.jpeg"

     # Check if the original image exists and delete it
    if os.path.exists(image_path):
        os.remove(image_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture an image.")
            break

        small_frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Press 'p' to take a photo", small_frame)

        key = cv2.waitKey(1)

        if key == ord('p' or 'P'):
            small_frame = cv2.resize(frame, (640, 480))
            cv2.imwrite(image_path, small_frame)
            print("Image captured and saved as 'image.jpeg'.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return image_path


def get_requests(string):

    url = f"https://api.d-id.com/talks/{string}"
    headers = {
        "accept": "application/json",
        "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
    }

    response = requests.get(url, headers=headers)
    print(response.text)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "done":
            print(data["result_url"])
    else:
        print("get_requests failed")


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
    print(s3_url)

    return s3_url


def post_requests(image_url):

    url = "https://api.d-id.com/talks"

    payload = {
        "script": {
            "type": "text",
            "input": "This is a test. And new for image uploading",
            "subtitles": "false",
            "provider": {
                "type": "microsoft",
                "voice_id": "en-US-DavisNeural",
                "voice_config": {
                    "style": "Whispering"
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
    print(response.text)

    if response.status_code == 201:
        data = response.json()
        print (data["id"])
        string = data["id"]

        # Wait for the image uploading to the platform
        time.sleep(20)
        get_requests(string)
    else:
        print("id request failed")


# At the beginning, capture an image and get its path
image_path = capture_and_save_image()

# Upload the image and get the image URL and Perform the POST request with the image URL
image_url = upload_image()
post_requests(image_url)