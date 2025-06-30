from fastapi import FastAPI
from database import engine, Base

app = FastAPI(
    title="Fruits Map API",
    description="API for Fruits Map project – fresh fruits, veggies and more in Gush Dan",
    version="0.1.0"
)

# Автоматическое создание таблиц, если их нет
Base.metadata.create_all(bind=engine)

# Корневой эндпоинт
@app.get("/")
def read_root():
    return {"message": "Fruits Map API is running"}
