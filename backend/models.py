from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    icon = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    places = relationship("Place", back_populates="category")


class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    description = Column(String)
    photo = Column(String, nullable=True)  # ✅ Фото
    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("Category", back_populates="places")
    reviews = relationship("Review", back_populates="place")


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    place_id = Column(Integer, ForeignKey("places.id"))
    rating = Column(Integer)
    comment = Column(String)
    author_name = Column(String, nullable=True)
    photo = Column(String, nullable=True)  # ✅ Фото
    created_at = Column(DateTime, default=datetime.utcnow)

    place = relationship("Place", back_populates="reviews")


class CategorySuggestion(Base):
    __tablename__ = "category_suggestions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
