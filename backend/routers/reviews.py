from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Review
from backend.schemas import Review, ReviewCreate
import crud

router = APIRouter()


@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db=db, review=review)


@router.get("/place/{place_id}", response_model=list[Review])
def get_reviews_by_place(place_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews_by_place(db, place_id)
