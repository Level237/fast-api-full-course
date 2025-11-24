from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()
books= [
    {
        "id":1,
        "title":"Think python",
        "author":"Al Sweigart",
        "publisher":"O'Reilly Media",
        "publisher_date":"2021-01-01",
        "page_count":1234,
        "language":"English"
    },
    {
        "id":2,
        "title":"Django by Example",
        "author":"Antonio Mele",
        "publisher":"level",
        "publisher_date":"2021-03-01",
        "page_count":1234,
        "language":"English"
    },{
        "id":3,
        "title":"Laravel by Example",
        "author":"Antonio Mele",
        "publisher":"Jimmy",
        "publisher_date":"2021-03-01",
        "page_count":1234,
        "language":"English"
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    publisher_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
    
@app.get("/books",response_model=List[Book])

async def get_all_books() -> list:
    return books

@app.post("/books",status_code=status.HTTP_201_CREATED)

async def create_a_book(book_data:Book) ->dict:
    newBook=book_data.model_dump()
    
    books.append(newBook)
    
    return newBook

@app.get("/book/{book_id}")

async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
@app.get("/book/{book_id}")

async def update_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book

@app.patch("/book/{book_id}")

async def update_book(book_id: int,book_data:BookUpdateModel) -> dict:
    
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['author'] = book_data.author
            book['publisher'] = book_data.publisher
            book['page_count'] = book_data.page_count
            book['language'] = book_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")

@app.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)

async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")