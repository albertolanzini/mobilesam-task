from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import io

from main import segment_everything

app = FastAPI()


# functional test performed through Postman at the endpoint http://127.0.0.1:8000/segment-image
@app.post("/segment-image/")
async def api_segment_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    segmented_image = segment_everything(image)
    segmented_image.save("temp_output.png")
    return FileResponse("temp_output.png")
