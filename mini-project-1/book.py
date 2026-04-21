from fastapi import APIRouter, HTTPException
from models import Book

router = APIRouter()

books = []

@router.get("/")
def get_books():
    return books

@router.get("/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post("/")
def add_book(book: Book):
    books.append(book)
    return book