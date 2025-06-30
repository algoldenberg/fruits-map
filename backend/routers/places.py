from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, desc, asc
from typing import List, Optional
import models, schemas
from database import get_db
from logger import logger
from auth import verify_admin_token
from backend.utils.file_utils import delete_file_if_unused



router = APIRouter(
    prefix="/places",
    tags=["Places"]
)


# 🔍 Поиск с фильтрами и географическими границами
@router.get("/search/", response_model=List[schemas.Place])
def search_places(
    db: Session = Depends(get_db),
    category_id: Optional[int] = None,
    min_rating: Optional[float] = None,
    has_photo: Optional[bool] = None,
    search: Optional[str] = None,
    lat_min: Optional[float] = None,
    lat_max: Optional[float] = None,
    lon_min: Optional[float] = None,
    lon_max: Optional[float] = None,
    sort_by: Optional[str] = Query("created_at", regex="^(name|created_at|rating)$"),
    order: Optional[str] = Query("desc", regex="^(asc|desc)$"),
):
    query = db.query(models.Place)

    # 🔍 Фильтр по категории
    if category_id is not None:
        query = query.filter(models.Place.category_id == category_id)

    # 🔍 Фильтр по наличию фото
    if has_photo is True:
        query = query.filter(models.Place.photo.isnot(None))

    # 🔍 Фильтр по поиску
    if search:
        query = query.filter(
            (models.Place.name.ilike(f"%{search}%")) |
            (models.Place.description.ilike(f"%{search}%"))
        )

    # 🔍 Фильтр по координатам
    if lat_min is not None and lat_max is not None:
        query = query.filter(models.Place.lat >= lat_min, models.Place.lat <= lat_max)

    if lon_min is not None and lon_max is not None:
        query = query.filter(models.Place.lon >= lon_min, models.Place.lon <= lon_max)

    # 🔍 Фильтр по рейтингу
    if min_rating is not None:
        avg_ratings = (
            db.query(models.Review.place_id, func.avg(models.Review.rating).label("avg_rating"))
            .group_by(models.Review.place_id)
            .subquery()
        )
        query = query.join(avg_ratings, models.Place.id == avg_ratings.c.place_id)
        query = query.filter(avg_ratings.c.avg_rating >= min_rating)

    # 🔄 Сортировка
    if sort_by == "rating":
        avg_ratings = (
            db.query(models.Review.place_id, func.avg(models.Review.rating).label("avg_rating"))
            .group_by(models.Review.place_id)
            .subquery()
        )
        query = query.outerjoin(avg_ratings, models.Place.id == avg_ratings.c.place_id)
        sort_column = avg_ratings.c.avg_rating
    elif sort_by == "name":
        sort_column = models.Place.name
    else:
        sort_column = models.Place.created_at

    if order == "desc":
        query = query.order_by(desc(sort_column))
    else:
        query = query.order_by(asc(sort_column))

    places = query.all()

    logger.info(f"{len(places)} places found with filters")

    return places


# 🔗 Получить все места
@router.get("/", response_model=List[schemas.Place])
def get_places(db: Session = Depends(get_db)):
    places = db.query(models.Place).all()
    logger.info("Retrieved all places")
    return places


# 🔗 Получить место по ID
@router.get("/{place_id}", response_model=schemas.Place)
def get_place(place_id: int, db: Session = Depends(get_db)):
    place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not place:
        logger.warning(f"Place {place_id} not found")
        raise HTTPException(status_code=404, detail="Place not found")
    logger.info(f"Retrieved place {place_id}")
    return place


# ➕ Создать место
@router.post("/", response_model=schemas.Place, dependencies=[Depends(verify_admin_token)])
def create_place(place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    logger.info(f"Created place {db_place.id}")
    return db_place


# ✏️ Обновить место
@router.put("/{place_id}", response_model=schemas.Place, dependencies=[Depends(verify_admin_token)])
def update_place(place_id: int, place: schemas.PlaceCreate, db: Session = Depends(get_db)):
    db_place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not db_place:
        logger.warning(f"Place {place_id} not found for update")
        raise HTTPException(status_code=404, detail="Place not found")

    for key, value in place.dict().items():
        setattr(db_place, key, value)

    db.commit()
    db.refresh(db_place)
    logger.info(f"Updated place {place_id}")
    return db_place


# 🗑️ Удалить место  
@router.delete("/{place_id}", dependencies=[Depends(verify_admin_token)])
def delete_place(place_id: int, db: Session = Depends(get_db)):
    db_place = db.query(models.Place).filter(models.Place.id == place_id).first()

    if not db_place:
        logger.warning(f"Place {place_id} not found for delete")
        raise HTTPException(status_code=404, detail="Place not found")

    # Удаляем фото, если оно больше нигде не используется
    if db_place.photo:
        delete_file_if_unused(db_place.photo, db)

    db.delete(db_place)
    db.commit()

    logger.info(f"Deleted place {place_id}")
    return {"message": "Place deleted"}
