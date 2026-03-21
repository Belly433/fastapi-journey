from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio

from book import router as book_router

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="templates")

# Include router
app.include_router(book_router, prefix="/books")

# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Books HTML page
@app.get("/books-page", response_class=HTMLResponse)
def books_page(request: Request):
    return templates.TemplateResponse("book.html", {"request": request})

# Async endpoint
books = []

@app.get("/books/delay/")
async def get_books_with_delay():
    await asyncio.sleep(1)
    return books


@app.get("/home", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/books/{book_id}/html", response_class=HTMLResponse)
def book_html(request: Request, book_id: int):
    return templates.TemplateResponse("book.html", {"request": request})