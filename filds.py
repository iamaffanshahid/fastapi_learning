from fastapi import FastAPI,Path,Query,HTTPException
from typing import Optional
from pydantic import BaseModel,Field
from starlette import status
app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:float
    publish_date:int

    def __init__(self,id,title,author,description,rating,publish_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.publish_date = publish_date




class BookRequest(BaseModel):
    id: Optional[int] = Field(default=None)
    title:str = Field(min_length=4)
    author:str = Field(min_length=4)
    description:str = Field(min_length=1,max_length=100)
    rating:float = Field(gt=-1,lt=11)
    publish_date:int = Field(gt=1999,lt=2025)

    class Config:
        json_schema_extra = {
            "example":{
                "title": "A new book",
                "author": "New author",
                "description": "A new description",
                "rating": 5,
                "publish_date": 2012
            }
        }



BOOKS = [

    Book(1, "science","A", "amazing",2.5,2012),
    Book(2,"History","B","amazing",5.5,2014),
    Book(3,"physics","C","amazing",3.5,2000),
    Book(4,"English","D","amazing",8.5,2006),
    Book(5,"urdu","E","amazing",1.5,2007),
    Book(6,"Math","F","amazing",9.5,2009)
]

@app.get("/books",status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}",status_code=status.HTTP_200_OK)
async def read_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404 , detail="item not found")
@app.get("/books/",status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating:float = Query(gt=0,lt=10)):
    book_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            book_to_return.append(book)
    return book_to_return


@app.post("/create_book",status_code=status.HTTP_204_NO_CONTENT)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    find_book_id(new_book)
    BOOKS.append(new_book)
    return new_book

def find_book_id(book:Book):
    book.id = 1 if len(BOOKS) == 0  else BOOKS[-1].id + 1

@app.put("/book/update_book",status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if  not book_changed:
        raise HTTPException(status_code=404 , detail="item not found")

@app.delete("/book/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    raise HTTPException(status_code=404 , detail="item not found")

@app.get("/books/publish/",status_code=status.HTTP_200_OK)
async def read_book_by_publish_date(publish_date:int = Query(gt=1999,lt=2025)):
    books_to_return = []
    for book in BOOKS:
        if book.publish_date == publish_date:
             books_to_return.append(book)
    return books_to_return
