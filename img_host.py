import base64
import requests
imgbb_api_token='effcec368f45e4712b6aa6b659a0f580'


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

# Example usage
with open("C:\\Users\\Kshit\\Desktop\\Pixelmate\\yellow_cat_on_park_bench.png", "rb") as file:
    image_file = file.read()

image_url = upload_image(image_file)
if image_url:
    print(f"Image URL: {image_url}")
else:
    print("Failed to upload image.")






