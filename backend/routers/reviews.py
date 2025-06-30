from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db
from logger import logger
from auth import verify_admin_token
from backend.utils.file_utils import delete_file_if_unused




router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


# ➕ Создать отзыв
@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    logger.info(f"Created review {db_review.id} for place {db_review.place_id}")
    return db_review


# 🔗 Получить все отзывы
@router.get("/", response_model=List[schemas.Review])
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(models.Review).all()
    logger.info("Retrieved all reviews")
    return reviews


# 🔗 Получить отзыв по ID
@router.get("/{review_id}", response_model=schemas.Review)
def get_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        logger.warning(f"Review {review_id} not found")
        raise HTTPException(status_code=404, detail="Review not found")
    logger.info(f"Retrieved review {review_id}")
    return review


# ✏️ Обновить отзыв
@router.put(
    "/{review_id}",
    response_model=schemas.Review,
    dependencies=[Depends(verify_admin_token)]
)
def update_review(review_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not db_review:
        logger.warning(f"Review {review_id} not found for update")
        raise HTTPException(status_code=404, detail="Review not found")

    for key, value in review.dict().items():
        setattr(db_review, key, value)

    db.commit()
    db.refresh(db_review)
    logger.info(f"Updated review {review_id}")
    return db_review


# 🗑️ Удалить отзыв
@router.delete(
    "/{review_id}",
    dependencies=[Depends(verify_admin_token)]
)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()

    if not db_review:
        logger.warning(f"Review {review_id} not found for delete")
        raise HTTPException(status_code=404, detail="Review not found")

    # Удаляем фото, если оно больше нигде не используется
    if db_review.photo:
        delete_file_if_unused(db_review.photo, db)

    db.delete(db_review)
    db.commit()

    logger.info(f"Deleted review {review_id}")
    return {"message": "Review deleted"}

