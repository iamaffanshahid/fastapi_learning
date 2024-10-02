from fastapi import Body,FastAPI

app = FastAPI()
BOOKS = [
    {"title":"Title one","author":"Author one","category":"Science"},
    {"title":"Title two","author":"Author two","category":"Science"},
    {"title":"Title three","author":"Author three","category":"History"},
    {"title":"Title four","author":"Author four","category":"Maths"},
    {"title":"Title five","author":"Author five","category":"English"}
]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title:str):   
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
        
@app.get("/books/{books_author}/")   
async def read_auther_category_by_query(author:str,category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold() and \
                book.get("author").casefold() == author.casefold():
             books_to_return.append(book)
    return  books_to_return
            
@app.post("/books/creat_book")
async def creat_book(new_book=Body()):
    BOOKS.append(new_book)            
