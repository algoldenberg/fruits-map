from pydantic import BaseModel, Field
from typing import Optional


# ================= Categories =================
class CategoryBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    icon: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# ================= Places =================
class PlaceBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    address: str = Field(..., min_length=3, max_length=200)
    lat: float = Field(..., ge=-90, le=90, description="Latitude must be between -90 and 90")
    lon: float = Field(..., ge=-180, le=180, description="Longitude must be between -180 and 180")
    category_id: int
    description: Optional[str] = Field(None, max_length=500)
    photo: Optional[str] = None


class PlaceCreate(PlaceBase):
    pass


class Place(PlaceBase):
    id: int

    class Config:
        from_attributes = True


# ================= Reviews =================
class ReviewBase(BaseModel):
    place_id: int
    rating: int = Field(..., ge=1, le=5, description="Rating must be between 1 and 5")
    comment: Optional[str] = Field(None, max_length=500)
    author_name: Optional[str] = Field(None, max_length=100)
    photo: Optional[str] = None


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int

    class Config:
        from_attributes = True


# ================= Category Suggestions =================
class CategorySuggestionBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = Field(None, max_length=300)


class CategorySuggestionCreate(CategorySuggestionBase):
    pass


class CategorySuggestion(CategorySuggestionBase):
    id: int

    class Config:
        from_attributes = True
