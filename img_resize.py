from PIL import Image
import os
import io
from img_host import upload_image

def resize_image(img_file, nw, nh):
    try:
        print("Opening image...")
        img = Image.open(img_file)
        
        print("Resizing image...")
        resized_img = img.resize((nw, nh))
        
        # Save the resized image to a bytes buffer
        buffer = io.BytesIO()
        resized_img.save(buffer, format="PNG")
        buffer.seek(0)
        
        print("Uploading resized image...")
        link = upload_image(buffer)
        
        print(f"Image uploaded, link: {link}")
        return {"image_url": link}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

