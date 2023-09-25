import requests



#--------------The GET request, using the URL generated after uploading the picture

def make_vid(id):
    # # URL is now https://api.d-id.com/talks/the_id_from_the_response_to_the_previous_POST_request

    #url = "https://api.d-id.com/talks/"+id
    headers = {
        "accept": "application/json",
        "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
    }

    response = requests.get(url, headers=headers)
    #print(response.text)

    if response.status_code==200:
        data=response.json()
        if (data["status"]=="done"): #I think the webhook purpose is to give us the response once the status is done. We need to check if theres a scenerio when its still "created" and then we have to loop until its done
            print (data["result_url"])
    else:
        print("make_vid request failed")




#-------------- 1. upload a picture from a local folder to create a URL 


# url = "https://api.d-id.com/images"

# #this is the line that handles the uploading, currently only with the GUI on the website
# files = { "image": ("shai-rapoport.jpeg", open("shai-rapoport.jpeg", "rb"), "image/jpeg") }

# headers = {
#     "accept": "application/json",
#     "content-type": "multipart/form-data",
#     "authorization": "Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# }

# response = requests.post(url, headers=headers)

# print(response.text)


#--------------The POST request, using the URL generated after uploading the picture

url = "https://api.d-id.com/talks"

payload = {
    "script": {
        "type": "text",
        "input": "This is test number two, with a python code! I have to say this is quite fun.. for now",
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

    "source_url": "s3://d-id-images-prod/google-oauth2|104050255703233554578/img_sgDO5_RMnPTtJ096dNNLG/shai-rapoport.jpeg"

}


headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Basic WjNwak1UTTBOekkxTWpjM056bEFaMjFoYVd3dVkyOXQ6c3gybnJjcnlsZTJSUzU3SXdTSXVM"
}

response = requests.post(url, json=payload, headers=headers)
# print(response.text)

if response.status_code==201:
    data=response.json()
    print (data["id"])
    make_vid(data["id"])
else:
    print("id request failed")




#-------------- The last part is playing the video. Pasting the "result url" from the response to the GET request downloads the video locally.
#so there needs to be a way to automatically download the video and play it from a folder I guess?





