from fastapi import Header, HTTPException

ADMIN_TOKEN = "supersecretadmintoken"  # Заменить на свой токен


def verify_admin_token(x_token: str = Header(...)):
    if x_token != ADMIN_TOKEN:
        raise HTTPException(status_code=403, detail="Admin privileges required")
