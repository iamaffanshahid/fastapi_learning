from fastapi import FastAPI
from pydantic import BaseModel,Field
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
    id:int = Field(gt=3)
    title:str = Field(min_length=4)
    author:str = Field(min_length=4)
    description:str = Field(min_length=1,max_length=100)
    rating:float = Field(gt=-1,lt=11)


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
    find_book_id(new_book)
    BOOKS.append(new_book)
    return new_book

def find_book_id(book:Book):
    book.id = 1 if len(BOOKS) == 0  else BOOKS[-1].id + 1