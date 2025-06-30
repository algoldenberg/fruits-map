import os
from fastapi import UploadFile
from uuid import uuid4

UPLOAD_FOLDER = "backend/static/uploads"

# Создание папки, если её нет
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_file(file: UploadFile) -> str:
    file_extension = file.filename.split(".")[-1]
    file_id = f"{uuid4()}.{file_extension}"
    file_path = os.path.join(UPLOAD_FOLDER, file_id)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return f"/static/uploads/{file_id}"
