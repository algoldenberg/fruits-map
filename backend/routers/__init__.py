from fastapi import APIRouter
from . import places, categories, reviews, category_suggestions

router = APIRouter()

router.include_router(places.router, prefix="/places", tags=["Places"])
router.include_router(categories.router, prefix="/categories", tags=["Categories"])
router.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
router.include_router(category_suggestions.router, prefix="/category-suggestions", tags=["Category Suggestions"])
