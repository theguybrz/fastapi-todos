from sqlalchemy.orm import Session
from app import models, schemas

def list_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo_in: schemas.TodoCreate):
    todo = models.Todo(title=todo_in.title, completed=todo_in.completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(db: Session, todo: models.Todo, data: schemas.TodoUpdate):
    if data.title is not None:
        todo.title = data.title
    if data.completed is not None:
        todo.completed = data.completed
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo: models.Todo):
    db.delete(todo)
    db.commit()