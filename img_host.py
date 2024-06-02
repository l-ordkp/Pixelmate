import base64
import requests
from dotenv import load_dotenv
load_dotenv()
import os
imgbb_api_token = os.getenv('IMG_BB_API_TOKEN')



import requests

def upload_image(image_file, api_key=imgbb_api_token, expiration=600):
    url = "https://api.imgbb.com/1/upload"
    params = {
        "key": api_key,
        "expiration": expiration
    }

    files = {
        "image": image_file
    }
    response = requests.post(url, params=params, files=files)
    response_data = response.json()

    if response_data.get("success"):
        image_url = response_data.get("data").get("url")
        
        return image_url
    else:
        return None







