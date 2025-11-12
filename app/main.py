from fastapi import FastAPI
from app.routers import todos
from app.db import init_db

app = FastAPI(title="FastAPI Todos", version="1.0.0")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(todos.router, prefix="/api/v1", tags=["todos"])

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}