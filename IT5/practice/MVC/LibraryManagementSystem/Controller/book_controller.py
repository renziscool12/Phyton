from LibraryManagementSystem.Models.book_model import BookModel

class BookController:
    def __init__(self):
        self.book_model = BookModel()

    def get_all_book(self):
        return self.book_model.get_all_books()

    def get_book_by_id(self,book_id):
        book = self.book_model.get_book(book_id)

        if not book:
            return None
        return book

    def add_book(self, title, author, description):
        book_id = self.book_model.add_book(title, author, description)
        return {"message":"Book added successfully", "book_id": book_id}

    def update_book(self, book_id, title,author,description):
        result = self.book_model.update_book(book_id, title, author, description)
        return result

    def delete_book(self, book_id):
        return self.book_model.delete_book(book_id)
