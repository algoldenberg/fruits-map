from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from database import engine, Base
from routers import router as api_router
from routers import files
from exceptions import custom_http_exception_handler, validation_exception_handler

app = FastAPI(
    title="Fruits Map API",
    description="API for Fruits Map project — fresh fruits, veggies and more in Gush Dan",
    version="0.2.0"
)

# ✅ Подключение статики
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
app.mount("/uploads", StaticFiles(directory="backend/static/uploads"), name="uploads")

# ✅ Настройка CORS (чтобы фронт спокойно делал запросы)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно ограничить доступ конкретными доменами фронта
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Создание таблиц базы данных (если их нет)
Base.metadata.create_all(bind=engine)

# ✅ Подключение всех роутеров
app.include_router(api_router)
app.include_router(files.router)

# ✅ Обработчики ошибок
app.add_exception_handler(StarletteHTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# ✅ Корневой эндпоинт
@app.get("/")
def read_root():
    return {"message": "Fruits Map API is running"}
