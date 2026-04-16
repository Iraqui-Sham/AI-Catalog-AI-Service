from fastapi import APIRouter, UploadFile, File
from app.services.remove_bg import remove_background
from app.services.align import align_image
from app.services.enhance import enhance_image
from app.services.bg import add_white_bg
from app.services.center import center_image
from app.services.shadow import add_shadow
import base64

router = APIRouter()

@router.post("/generate")
async def generate(file: UploadFile = File(...)):
    
    contents = await file.read()

    # STEP 1: remove bg
    img = remove_background(contents)

    # STEP 2: align
    img = align_image(img)

    # STEP 3: white background
    img = add_white_bg(img)

    img = center_image(img)
    
    img = add_shadow(img)   

    # STEP 4: enhance
    img = enhance_image(img)

    # convert to base64
    import io
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue()).decode()

    return {
        "image": f"data:image/jpeg;base64,{img_str}"
    }