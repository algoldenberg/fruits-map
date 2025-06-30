import os
from models import Place, Review


def delete_file_if_unused(filename: str, db):
    if not filename:
        return

    used_in_places = db.query(Place).filter(Place.photo == filename).count()
    used_in_reviews = db.query(Review).filter(Review.photo == filename).count()

    if used_in_places + used_in_reviews == 0:
        file_path = os.path.join("media", filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted file {file_path}")
        else:
            print(f"File {file_path} not found")
