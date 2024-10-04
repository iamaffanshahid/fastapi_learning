from fastapi import FastAPI,Body
from pydantic import BaseModel
app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating




class BookRequest(BaseModel):
    id:int
    title:str
    author:str
    description:str
    rating:int


BOOKS = [
    Book(1,"science","A","amazing",2.5),
    Book(2,"History","B","amazing",5.5),
    Book(3,"physics","C","amazing",3.5),
    Book(4,"English","D","amazing",8.5),
    Book(5,"urdu","E","amazing",1.5),
    Book(6,"Math","F","amazing",9.5)
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(book_request:BookRequest):

    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)