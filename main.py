from fastapi import FastAPI, File, UploadFile
     import easyocr
     import uvicorn
     import numpy as np
     from PIL import Image
     import io

     app = FastAPI()
     reader = easyocr.Reader(['en'])

     @app.post("/")
     async def read_text(file: UploadFile = File(...)):
         contents = await file.read()
         image = Image.open(io.BytesIO(contents))
         image_np = np.array(image)
         result = reader.readtext(image_np)
         texts = [entry[1] for entry in result]
         return {"texts": texts}

     if __name__ == "__main__":
         uvicorn.run(app, host="0.0.0.0", port=3000)