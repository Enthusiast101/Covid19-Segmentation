import io
import base64
import numpy as np
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from PIL import Image

app = FastAPI()

MODEL_PATH = "models/UNet.h5"
model = tf.keras.models.load_model(MODEL_PATH)

@app.get("/", response_class=HTMLResponse)
async def index():
    return f"Response-200"


@app.post("/model")
async def data(image: UploadFile = File(...)):
    try:
        image_bytes = await image.read()
        img = Image.open(io.BytesIO(image_bytes)).convert("L")
        
        img = img.resize((128, 128))
        img = np.asarray(img)[..., np.newaxis][np.newaxis, ...]

        pred = model.predict(img)
        pred = np.squeeze(pred)
        pred = (pred * 255).clip(0, 255).astype(np.uint8)
        pred_img = Image.fromarray(pred, mode="L")

        buffer = io.BytesIO()
        pred_img.save(buffer, format="PNG")
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return JSONResponse(content={"success": True, "image": image_base64}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"success": False, "error": str(e)}, status_code=500)

