from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
import os
from img_resize import resize_image
from pydantic import BaseModel
from api_runwayml import runway_ml
from img_host import upload_image
from img_resize import resize_image

app = FastAPI()

@app.post("/resize-image/")
async def resize_image_endpoint(
    test_img: UploadFile = File(...),
    new_width: int = Form(...),
    new_height: int = Form(...)
):
    res = resize_image(test_img.file, new_width, new_height)
    return res

@app.post("/inpaint")
async def inpaint(prompt: str = Form(...), image: UploadFile = File(...), mask: UploadFile = File(...)):
    output = runway_ml(image.file, mask.file, prompt)
    return output



