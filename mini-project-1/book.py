from fastapi import APIRouter, HTTPException
from models import Book
from database import managed_db

router = APIRouter()



@router.get("/")
def get_books():
    with managed_db() as db:
        return db.get_all()
    

@router.get("/{book_id}")
def get_book(book_id: int):
    with managed_db() as db:
        book = db.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

@router.post("/")
def add_book(book: Book):
    with managed_db() as db:
        new_id = db.create(book)
        return {"id": new_id}
    
@router.put("/{book_id}")
def update_book(book_id: int, book: Book):
    with managed_db() as db:
        updated = db.update(book_id, book)
        if not updated:
            raise HTTPException(status_code=404, detail="Book not found")
        return updated
    
@router.delete("/{book_id}")
def delete_book(book_id: int):
    with managed_db() as db:
        db.delete(book_id)
        return {"message": "deleted"}