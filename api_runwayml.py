import os
from dotenv import load_dotenv
load_dotenv()
replicate_api_token = os.getenv('REPLICATE_API_TOKEN')
import replicate
from img_host import upload_image

def runway_ml(img,mask_img,prompt):
    input = {
        "mask": upload_image(mask_img),
        "image": upload_image(img),
        "prompt": prompt
    }

    output = replicate.run(
        "andreasjansson/stable-diffusion-inpainting:e490d072a34a94a11e9711ed5a6ba621c3fab884eda1665d9d3a282d65a21180",
        input=input
    )
    return output