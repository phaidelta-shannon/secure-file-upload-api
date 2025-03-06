# Secure File Upload API

This project demonstrates user authentication and secure file uploads using **FastAPI** for the backend and **NiceGUI** for the frontend.

---

## Setup Instructions

1. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment**:
   ```bash
   venv\Scripts\activatepython -m venv venv
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Check SQLite Version**:
   ```bash
   python -c "import sqlite3; print(sqlite3.sqlite_version)"
   ```
5. **Initialize the Database:**:
   ```bash
   python -c "from backend.database import init_db; init_db()"
   ```
6. **Run the Backend Server**:
   ```bash
   uvicorn backend.main:app --reload
   ```
7. **Run the Frontend Application:**:
   ```bash
   python frontend/app.py
   ```
## Project Structure
```
secure-file-upload-api/
│── backend/
│   │── main.py            # FastAPI application entry point
│   │── auth.py            # User authentication logic
│   │── file_upload.py     # File upload handling logic
│   │── database.py        # Database initialization and operations
│── frontend/
│   │── app.py             # NiceGUI frontend application
│── uploads/               # Directory created at runtime for storing uploaded files
│── venv/                  # Virtual environment directory (created after setup)
│── files.db               # SQLite database file (created after initializing the database)
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── .gitignore             # Specifies files and directories to ignore in version control
```

## Key Features
1. User Authentication: Secure user login and registration.

2. File Uploads: Allows users to upload files securely.

3. Database: SQLite database for storing user and file metadata.

4. Frontend: NiceGUI-based frontend for interacting with the backend.

## Notes
- The uploads/ directory is created at runtime to store uploaded files.
- The files.db SQLite database is created after running the init_db() function.
- Ensure the virtual environment is activated before running any commands.
