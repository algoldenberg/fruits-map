from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import CategorySuggestion
from backend.schemas import CategorySuggestion, CategorySuggestionCreate
import crud

router = APIRouter()


@router.post("/", response_model=CategorySuggestion)
def create_suggestion(suggestion: CategorySuggestionCreate, db: Session = Depends(get_db)):
    return crud.create_category_suggestion(db=db, suggestion=suggestion)


@router.get("/", response_model=list[CategorySuggestion])
def read_suggestions(db: Session = Depends(get_db)):
    return crud.get_category_suggestions(db)
