from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud, database

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/", response_model=list[schemas.Category])
def read_categories(db: Session = Depends(database.SessionLocal)):
    return crud.get_categories(db)


@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_category(db=db, category=category)


@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(database.SessionLocal)):
    return crud.get_category(db=db, category_id=category_id)
