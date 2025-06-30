from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud, database

router = APIRouter(
    prefix="/places",
    tags=["Places"]
)


@router.get("/", response_model=list[schemas.Place])
def read_places(db: Session = Depends(database.SessionLocal)):
    return crud.get_places(db)


@router.post("/", response_model=schemas.Place)
def create_place(place: schemas.PlaceCreate, db: Session = Depends(database.SessionLocal)):
    return crud.create_place(db=db, place=place)


@router.get("/{place_id}", response_model=schemas.Place)
def read_place(place_id: int, db: Session = Depends(database.SessionLocal)):
    return crud.get_place(db=db, place_id=place_id)
