# 🥭 Fruits Map API

Интерактивная карта для поиска мест с фруктами, овощами и фермерскими продуктами в Гуш-Дане.  
Backend построен на FastAPI + PostgreSQL (Supabase).

---

## 🚀 Функциональность

- 📍 Категории (CRUD + предложения новых категорий от пользователей)
- 📍 Места (CRUD, поиск, фильтрация, сортировка)
- ⭐️ Отзывы с рейтингами и фото
- 📤 Загрузка изображений
- 🔑 Авторизация для админов через токен
- 🛑 Валидация данных и обработка ошибок
- 📜 Логирование всех действий
- 🗂️ Хранение файлов на сервере (`/static/uploads/`)

---

## 🗂️ Структура проекта

```
backend/
│
├── routers/              # Роутеры (places, categories, reviews, files и др.)
├── utils/                # Вспомогательные функции
├── static/uploads/       # Загруженные изображения
├── logs/                 # Логи
├── database.py           # Подключение к базе
├── models.py             # SQLAlchemy модели
├── schemas.py            # Pydantic схемы
├── exceptions.py         # Обработчики ошибок
├── logger.py             # Логирование
├── auth.py               # Авторизация
├── main.py               # Главный файл FastAPI-приложения
```

---

## ⚙️ Как запустить проект

### 1. Клонируем репозиторий

```bash
git clone https://github.com/yourusername/fruits-map.git
cd fruits-map/backend
```

### 2. Устанавливаем зависимости

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# или
source .venv/bin/activate      # Mac/Linux

pip install -r requirements.txt
```

### 3. Настраиваем переменные окружения

Создаем файл `.env`:

```env
DATABASE_URL=postgresql://postgres:[YOUR_PASSWORD]@db.[YOUR_SUPABASE].supabase.co:5432/postgres
ADMIN_TOKEN=[YOUR_SECRET_ADMIN_TOKEN]
```

### 4. Запуск приложения

```bash
uvicorn main:app --reload
```

### 5. Открываем в браузере:

- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc → [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🌍 Базовый URL

```
http://localhost:8000
```

---

## 🛡️ Авторизация (только для админов)

Для действий администратора (создание, изменение, удаление) нужно добавить в заголовки:

```
X-Token: [YOUR_ADMIN_TOKEN]
```

Все GET-запросы доступны без авторизации.

---

## 📦 Основные эндпоинты

| Модуль     | Эндпоинт                        | Описание                                |
|-------------|----------------------------------|------------------------------------------|
| 🔍 Places      | `/places/`                      | CRUD для мест                           |
| 🔍 Places      | `/places/search/`               | Поиск мест по фильтрам и сортировке      |
| 📚 Categories  | `/categories/`                  | CRUD для категорий                      |
| ⭐️ Reviews     | `/reviews/`                     | CRUD для отзывов                        |
| 📥 Files       | `/files/upload/`                | Загрузка изображений                    |
| 💡 Suggestions | `/category-suggestions/`        | Предложения новых категорий             |

---

## 🔍 Поиск мест

```
GET /places/search/
```

### Параметры (любые опционально):

| Параметр   | Описание                                      |
|-------------|-----------------------------------------------|
| category_id | Фильтр по категории                           |
| min_rating  | Фильтр по минимальному рейтингу               |
| has_photo   | true / false — фильтр по наличию фото         |
| search      | Поиск по названию и описанию                  |
| sort_by     | name / created_at / rating                    |
| order       | asc / desc                                    |

---

## 🏗️ Категории

- Получить список всех категорий:

```
GET /categories/
```

- Получить места по категории:

```
GET /places/search/?category_id=ID
```

---

## ⭐️ Добавить отзыв

```
POST /reviews/
```

### Пример тела запроса:

```json
{
  "place_id": 1,
  "rating": 5,
  "comment": "Отличное место!",
  "author_name": "Саша",
  "photo": "http://localhost:8000/uploads/uuid.jpg"
}
```

---

## 📤 Загрузка изображений

```
POST /files/upload/
```

### Формат Form-Data:

| Ключ  | Значение     |
|-------|---------------|
| file  | Изображение (.jpg, .png, .webp) |

### Ответ:

```json
{
  "filename": "uuid.jpg",
  "url": "/uploads/uuid.jpg"
}
```

---

## 🖼️ Работа с изображениями

- Все загруженные изображения доступны по URL:

```
http://localhost:8000/uploads/filename.jpg
```

---

## 🗑️ Админ-действия

Для всех POST, PUT, DELETE-запросов к категориям, местам и отзывам требуется заголовок:

```
X-Token: [YOUR_ADMIN_TOKEN]
```

---

## ✅ Примеры ошибок

```json
{
  "status": "error",
  "code": 404,
  "message": "Place not found"
}
```

---

## 🏗️ Документация API доступна по адресу:

```
http://localhost:8000/docs
```

---

## 🏗️ Стек технологий

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL (Supabase)
- Uvicorn

---

## 📜 Лицензия

MIT License

---

## 🔥 Контакты

Проект: **Fruits Map**  
Автор: **Саша Гольденберг**  
GitHub: [https://github.com/yourusername](https://github.com/yourusername)  
Telegram: [@goldenberga](https://t.me/goldenberga)