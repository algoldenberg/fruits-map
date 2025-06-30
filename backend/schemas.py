from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


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
        from_attributes = True


class PlaceBase(BaseModel):
    name: str
    address: Optional[str] = None
    lat: float
    lon: float
    description: Optional[str] = None
    category_id: int


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ReviewBase(BaseModel):
    place_id: int
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    author_name: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CategorySuggestionBase(BaseModel):
    name: str
    description: Optional[str] = None
    author_name: Optional[str] = None


class CategorySuggestionCreate(CategorySuggestionBase):
    pass


class CategorySuggestion(CategorySuggestionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
