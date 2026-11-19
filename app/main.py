from fastapi import FastAPI

from .routers import auth as auth_router
from .routers import categories, expenses

app = FastAPI(title="Expense Tracker API")

app.include_router(auth_router.router)
app.include_router(categories.router)
app.include_router(expenses.router)


@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}