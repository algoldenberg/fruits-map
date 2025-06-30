from fastapi import FastAPI
from database import engine, Base
from routers import router as api_router

app = FastAPI(
    title="Fruits Map API",
    description="API for Fruits Map project — fresh fruits, veggies and more in Gush Dan",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Fruits Map API is running"}
