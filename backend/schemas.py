from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# ===== Category =====

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ===== Review =====

class ReviewBase(BaseModel):
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    author_name: Optional[str] = None


class ReviewCreate(ReviewBase):
    place_id: int


class Review(ReviewBase):
    id: int
    created_at: datetime
    place_id: int

    class Config:
        orm_mode = True


# ===== Place =====

class PlaceBase(BaseModel):
    name: str
    address: Optional[str] = None
    lat: float
    lon: float
    description: Optional[str] = None
    category_id: Optional[int] = None


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int
    created_at: datetime
    category: Optional[Category] = None
    reviews: List[Review] = []

    class Config:
        orm_mode = True
