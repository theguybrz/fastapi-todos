from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.db import get_db
from app import schemas, crud

router = APIRouter()

@router.get("/todos", response_model=list[schemas.TodoOut])
def list_todos(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
):
    return crud.list_todos(db, skip=skip, limit=limit)

@router.post("/todos", response_model=schemas.TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo_in)

@router.get("/todos/{todo_id}", response_model=schemas.TodoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.patch("/todos/{todo_id}", response_model=schemas.TodoOut)
def update_todo(todo_id: int, data: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo(db, todo, data)

@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    crud.delete_todo(db, todo)
    return