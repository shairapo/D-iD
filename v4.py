import requests
import json
import time

#--------------The GET request, using the URL generated after uploading the picture

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


#-------------- 1. Upload a picture from a local folder to create a URL 

def upload_image():
    url = "https://api.d-id.com/images"

    #this is the line that handles the uploading, currently only with the GUI on the website
    files = { "image": ("shai-rapoport.jpeg", open("shai-rapoport.jpeg", "rb"), "image/jpeg") }

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


#-------------- 2. The POST request, using the URL generated after uploading the picture

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

    #     #the webhook line is not clear to me yet: "A webhook URL for sending the payload including animate details
    #     #In a case of empty value, the webhook will not be triggered"
        
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


# Upload the image and get the image URL and Perform the POST request with the image URL
image_url = upload_image()
post_requests(image_url)