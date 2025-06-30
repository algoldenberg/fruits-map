from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Place
from backend.schemas import Place, PlaceCreate
import crud

router = APIRouter()


@router.post("/", response_model=Place)
def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    return crud.create_place(db=db, place=place)


@router.get("/", response_model=list[Place])
def read_places(db: Session = Depends(get_db)):
    return crud.get_places(db)


@router.get("/{place_id}", response_model=Place)
def read_place(place_id: int, db: Session = Depends(get_db)):
    return crud.get_place(db, place_id)
