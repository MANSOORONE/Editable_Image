from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from utils.segmentation import get_masks
from utils.svg_generator import generate_svg_from_masks

app = FastAPI()

# ✅ CORS (important)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):
    
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ✅ NEW PIPELINE
    masks = get_masks(file_path)
    svg_path = generate_svg_from_masks(masks, file_path)

    return {"svg_file": svg_path}