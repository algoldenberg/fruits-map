from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Category
from backend.schemas import Category, CategoryCreate
import crud

router = APIRouter()


@router.post("/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)


@router.get("/", response_model=list[Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    return crud.get_category(db, category_id)
