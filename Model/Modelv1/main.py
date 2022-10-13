import shutil
from typing import Optional

from fastapi import FastAPI, File, UploadFile
from LipNet.lipnetfastapi import predict 
app = FastAPI()


@app.post("/")
def root(file: UploadFile= File(...)):
    with open(f'C:\\Users\\A\\Desktop\\Modelv1\\LipNet\\videos\\{file.filename}',"wb")as buffer:
        shutil.copyfileobj(file.file, buffer)

    return{"file_name": file.filename}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile= File(...)):
    return {"filename": file.filename}

@app.get("/")
def returnPredict():
     return {"name":predict.runs()}


     #1-   ngrok http 8000
     # 2- in api>> uvicorn --host + url from ngrok
     #3- uvicorn main:app --reload