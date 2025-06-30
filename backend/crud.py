from sqlalchemy.orm import Session
from models import Place, Category, Review, CategorySuggestion
from schemas import PlaceCreate, CategoryCreate, ReviewCreate, CategorySuggestionCreate


# ---------- Places ----------
def create_place(db: Session, place: PlaceCreate):
    db_place = Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


def get_places(db: Session):
    return db.query(Place).all()


def get_place(db: Session, place_id: int):
    return db.query(Place).filter(Place.id == place_id).first()


# ---------- Categories ----------
def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_categories(db: Session):
    return db.query(Category).all()


def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


# ---------- Reviews ----------
def create_review(db: Session, review: ReviewCreate):
    db_review = Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews_by_place(db: Session, place_id: int):
    return db.query(Review).filter(Review.place_id == place_id).all()


# ---------- Category Suggestions ----------
def create_category_suggestion(db: Session, suggestion: CategorySuggestionCreate):
    db_suggestion = CategorySuggestion(**suggestion.dict())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion


def get_category_suggestions(db: Session):
    return db.query(CategorySuggestion).all()
