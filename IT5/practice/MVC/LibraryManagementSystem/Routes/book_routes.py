from fastapi import HTTPException, APIRouter
from LibraryManagementSystem.Controller.book_controller import BookController
from LibraryManagementSystem.Schemas.book_schemas import BookCreate, BookUpdate

router = APIRouter()
controller = BookController()

@router.get('/')
def home():
    return {'message': 'API is running!'}

@router.get('/books')
def get_books():
    return controller.get_all_book()

@router.get('/books/{book_id}')
def get_book_by_id(book_id: int):
    book = controller.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail='Book not found')
    return book

@router.post('/books', status_code=201)
def create_book(book: BookCreate):
    return controller.add_book(book.title, book.author, book.description)

@router.put('/books/{book_id}')
def update_book(book_id: int, book: BookUpdate):
    result = controller.update_book(book_id, book.title, book.author, book.description)

    if result == 0:
        raise HTTPException(status_code=404, detail='Book not found')
    return {"message": "Book updated"}

@router.delete('/books/{book_id}')
def delete_book(book_id: int):
    result = controller.delete_book(book_id)
    if result == 0:
        raise HTTPException(status_code=404, detail='Book not found')
    return {"message": "Book deleted"}
