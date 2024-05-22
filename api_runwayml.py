import os
from dotenv import load_dotenv
load_dotenv()
replicate_api_token = os.getenv('REPLICATE_API_TOKEN')
import replicate

input = {
    "mask": "https://replicate.delivery/mgxm/188d0097-6a6f-4488-a058-b0b7a66e5677/desktop-mask.png",
    "image": "https://replicate.delivery/mgxm/f8c9cb3a-8ee8-41a7-9ef6-c65b37acc8af/desktop.png",
    "prompt": "a herd of grazing sheep"
}

output = replicate.run(
    "andreasjansson/stable-diffusion-inpainting:e490d072a34a94a11e9711ed5a6ba621c3fab884eda1665d9d3a282d65a21180",
    input=input
)
print(output)

