from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

import crud
from database import get_db
from schemas import CategorySuggestion, CategorySuggestionCreate
from logger import logger

ADMIN_TOKEN = "supersecretadmintoken"

router = APIRouter()


def verify_admin(x_token: str = Header(...)):
    if x_token != ADMIN_TOKEN:
        logger.warning("Unauthorized admin token attempt")
        raise HTTPException(status_code=403, detail="Not authorized")


@router.get("/", response_model=list[CategorySuggestion])
def read_category_suggestions(db: Session = Depends(get_db)):
    logger.info("Retrieved all category suggestions")
    return crud.get_category_suggestions(db)


@router.post("/", response_model=CategorySuggestion)
def create_category_suggestion(suggestion: CategorySuggestionCreate, db: Session = Depends(get_db)):
    new_suggestion = crud.create_category_suggestion(db, suggestion)
    logger.info(f"New category suggestion created: {suggestion.name}")
    return new_suggestion


@router.delete("/{suggestion_id}", dependencies=[Depends(verify_admin)])
def delete_category_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    result = crud.delete_category_suggestion(db, suggestion_id)
    if not result:
        logger.error(f"Suggestion with id {suggestion_id} not found")
        raise HTTPException(status_code=404, detail="Suggestion not found")
    logger.info(f"Suggestion with id {suggestion_id} deleted")
    return {"ok": True}
