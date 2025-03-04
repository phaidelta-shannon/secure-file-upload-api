from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from backend.auth import verify_api_key
from backend.file_upload import save_files
from backend.database import init_db, SessionLocal, FileRecord
import os

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
init_db()

@app.get("/")
def read_root(api_key: str = Depends(verify_api_key)):
    return {"message": "Welcome to the Secure File Upload API!"}

@app.post("/upload/")
def upload_files(files: list[UploadFile] = File(...), api_key: str = Depends(verify_api_key)):
    saved_files = save_files(files, UPLOAD_DIR)
    db = SessionLocal()
    for filename in saved_files:
        db.add(FileRecord(filename=filename))
    db.commit()
    return {"message": "Files uploaded successfully", "files": saved_files}