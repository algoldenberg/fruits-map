from sqlalchemy.orm import Session
from models import Category, Place, Review, CategorySuggestion


# ---------- Category ----------
def get_categories(db: Session):
    return db.query(Category).all()


def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def create_category(db: Session, category):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def update_category(db: Session, category_id: int, category):
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    for key, value in category.dict().items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category


def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if not db_category:
        return None
    db.delete(db_category)
    db.commit()
    return db_category


# ---------- Place ----------
def get_places(db: Session):
    return db.query(Place).all()


def get_place(db: Session, place_id: int):
    return db.query(Place).filter(Place.id == place_id).first()


def create_place(db: Session, place):
    db_place = Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


def delete_place(db: Session, place_id: int):
    place = get_place(db, place_id)
    if not place:
        return None
    db.delete(place)
    db.commit()
    return place


# ---------- Review ----------
def create_review(db: Session, review):
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews_by_place(db: Session, place_id: int):
    return db.query(Review).filter(Review.place_id == place_id).all()


# ---------- Category Suggestions ----------
def create_category_suggestion(db: Session, suggestion):
    db_suggestion = CategorySuggestion(**suggestion.dict())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion


def get_category_suggestions(db: Session):
    return db.query(CategorySuggestion).all()


def delete_category_suggestion(db: Session, suggestion_id: int):
    suggestion = db.query(CategorySuggestion).filter(CategorySuggestion.id == suggestion_id).first()
    if suggestion:
        db.delete(suggestion)
        db.commit()
        return True
    return False
