from sqlalchemy.orm import Session
import models, schemas


# ===== CATEGORY =====

def get_categories(db: Session):
    return db.query(models.Category).all()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


# ===== PLACE =====

def get_places(db: Session):
    return db.query(models.Place).all()


def get_place(db: Session, place_id: int):
    return db.query(models.Place).filter(models.Place.id == place_id).first()


def create_place(db: Session, place: schemas.PlaceCreate):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


# ===== REVIEW =====

def get_reviews_by_place(db: Session, place_id: int):
    return db.query(models.Review).filter(models.Review.place_id == place_id).all()


def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
