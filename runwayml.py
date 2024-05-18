from diffusers import StableDiffusionInpaintPipeline
import torch
from PIL import Image

# Load the pipeline without specifying torch_dtype
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting"
)

# Move the pipeline to CPU
pipe = pipe.to("cpu")

# Define the prompt
prompt = "Pikachu sitting on a park bench, high resolution"

# Load the images
image_path = r"C:\\Users\\Kshit\\Desktop\\Pixelmate\\image.png"
mask_image_path = r"C:\\Users\\Kshit\\Desktop\\Pixelmate\\mask_image.png"
image = Image.open(image_path).convert("RGB")
mask_image = Image.open(mask_image_path).convert("RGB")

# Run the pipeline
result = pipe(prompt=prompt, image=image, mask_image=mask_image).images[0]

# Save the result
result.save("./Pikachu.jpg")
