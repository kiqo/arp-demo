from functools import lru_cache
from typing import List

from fastapi import Depends, FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from loguru import logger
import uvicorn

from arpdemo import config
from arpdemo.helper import write

app = FastAPI()


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/settings")
async def settings(settings: config.Settings = Depends(get_settings)):
    return {"app_name": settings.app_name, "data_folder": settings.data_folder}


@app.get("/upload")
async def upload():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...),
                       settings: config.Settings = Depends(get_settings)):
    filenames = [f.filename for f in files]
    logger.info(f"/uploadfile/ called for files {filenames}")

    for file in files:
        content = await file.read()
        await write(settings.data_folder / file.filename, content)
    return {"message": "upload successful", "filenames": filenames}


if __name__ == '__main__':
    # TODO: reload=True only for development
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)
