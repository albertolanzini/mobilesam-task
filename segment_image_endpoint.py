from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
import io

from main import segment_everything

app = FastAPI()


# functional test performed through Postman at the endpoint http://127.0.0.1:8000/segment-image
@app.post("/segment-image/")
async def api_segment_image(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    segmented_image = segment_everything(image)

    buf = io.BytesIO()
    segmented_image.save(buf, format='PNG')
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
