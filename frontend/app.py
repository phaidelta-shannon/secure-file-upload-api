from nicegui import ui
import requests

API_KEY = "mysecureapikey"
BACKEND_URL = "http://127.0.0.1:8000"

# Function to upload files to backend
def upload_files(event):
    file = event  # 'event' itself contains the file details
    files_to_upload = [("files", (file.name, file.content.read(), file.type))]  # Read file content
    
    headers = {"api_key": API_KEY}
    response = requests.post(f"{BACKEND_URL}/upload/", files=files_to_upload, headers=headers)
    
    if response.status_code == 200:
        ui.notify(f"✅ {file.name} uploaded successfully", type='positive')
    else:
        error_message = response.json().get('detail', 'Upload failed')
        ui.notify(f"❌ Upload failed: {error_message}", type='negative')

# Function to check authentication status
def check_auth():
    headers = {"api_key": API_KEY}
    response = requests.get(f"{BACKEND_URL}/", headers=headers)

    with ui.row():
        if response.status_code == 200:
            ui.label("Authenticated").classes("text-green-600 text-lg font-bold")
        else:
            ui.label("Access Denied").classes("text-red-600 text-lg font-bold")

# UI Layout
with ui.column().classes("w-full items-center justify-center p-5"):
    ui.label("Secure File Upload API Demo").classes("text-2xl font-bold mb-2")

    # Authentication Status
    check_auth()

    # Upload Instructions
    ui.label(
        "📄 Please upload your files in PDF, XLSX, or XLS format.\n"
        "📏 Maximum file size: 10MB.\n"
        "📂 You can select multiple files at once."
    ).classes("text-lg mt-4 mb-1 text-gray-700")

    # Full-width upload button with a simple look
    ui.upload(on_upload=upload_files, multiple=True).classes("w-full border cursor-pointer")

# Run UI
ui.run(title="Secure File Upload", reload=True)
