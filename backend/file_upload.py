from fastapi import UploadFile, HTTPException
import shutil
import os

def save_files(files: list[UploadFile], upload_dir: str):
    allowed_extensions = {"pdf", "xlsx", "xls"}
    saved_files = []
    
    for file in files:
        ext = file.filename.split(".")[-1]
        if ext not in allowed_extensions:
            raise HTTPException(status_code=400, detail=f"File type {ext} not allowed")
        
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        saved_files.append(file.filename)
    return saved_files