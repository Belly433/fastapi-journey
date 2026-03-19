from fastapi import FastAPI
from models import Book
import asyncio

app = FastAPI()

books = []

@app.get("/books/")
async def get_books():
    return books

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books/")
async def add_book(book: Book):
    books.append(book)
    return book

@app.put("/books/{book_id}")
async def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"error": "Book not found"}

@app.get("/books/delay/")
async def get_books_with_delay():
    await asyncio.sleep(1)
    return books