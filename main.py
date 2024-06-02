from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import os
from img_resize import resize_image
from pydantic import BaseModel
from api_runwayml import runway_ml
from img_host import upload_image


app = FastAPI()

@app.post("/resize-image/")
async def resize_image(
    file: UploadFile = File(...),
    new_width: int = Form(...),
    new_height: int = Form(...)
):
    # Ensure the uploads directory exists
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
        
    input_path = f"uploads/{file.filename}"
    
    # Save the uploaded file
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # Define the output path
    output_path = f"uploads/resized_{file.filename}"

    # Resize the image using the imported function
    resize_image(input_path, output_path, new_width, new_height)

    return FileResponse(output_path, media_type="image/jpeg", filename=f"resized_{file.filename}")


# To run the app, use the command: uvicorn main:app --reload


@app.post("/inpaint")
async def inpaint(prompt: str = Form(...), image: UploadFile = File(...), mask: UploadFile = File(...)):
    output = runway_ml(image.file, mask.file, prompt)
    return output



