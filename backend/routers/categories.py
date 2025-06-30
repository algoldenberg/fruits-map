from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

import crud
from database import get_db
from schemas import Category, CategoryCreate, CategoryBase
from logger import logger
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

import models
import schemas
from database import get_db
from logger import logger
from auth import verify_admin_token



ADMIN_TOKEN = "supersecretadmintoken"

router = APIRouter()


def verify_admin(x_token: str = Header(...)):
    if x_token != ADMIN_TOKEN:
        logger.warning("Unauthorized admin token attempt")
        raise HTTPException(status_code=403, detail="Not authorized")


@router.get("/", response_model=list[Category])
def read_categories(db: Session = Depends(get_db)):
    logger.info("Retrieved all categories")
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if not category:
        logger.error(f"Category with id {category_id} not found")
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Retrieved category with id {category_id}")
    return category


@router.post("/", response_model=Category, dependencies=[Depends(verify_admin)])
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = crud.create_category(db, category)
    logger.info(f"New category created: {category.name}")
    return new_category


@router.put("/{category_id}", response_model=Category, dependencies=[Depends(verify_admin)])
def update_category(category_id: int, category: CategoryBase, db: Session = Depends(get_db)):
    result = crud.update_category(db, category_id, category)
    if not result:
        logger.error(f"Category with id {category_id} not found")
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Category with id {category_id} updated")
    return result


@router.delete("/{category_id}", dependencies=[Depends(verify_admin)])
def delete_category(category_id: int, db: Session = Depends(get_db)):
    result = crud.delete_category(db, category_id)
    if not result:
        logger.error(f"Category with id {category_id} not found")
        raise HTTPException(status_code=404, detail="Category not found")
    logger.info(f"Category with id {category_id} deleted")
    return {"ok": True}


@router.get("/{category_id}/places", response_model=List[schemas.Place])
def get_places_by_category(category_id: int, db: Session = Depends(get_db)):
    places = db.query(models.Place).filter(models.Place.category_id == category_id).all()

    if not places:
        logger.info(f"No places found for category_id {category_id}")
    else:
        logger.info(f"{len(places)} places found for category_id {category_id}")

    return places
