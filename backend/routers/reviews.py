from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud, database

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.post("/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_review(db=db, review=review)


@router.get("/place/{place_id}", response_model=list[schemas.Review])
def read_reviews_by_place(place_id: int, db: Session = Depends(database.SessionLocal)):
    return crud.get_reviews_by_place(db=db, place_id=place_id)
