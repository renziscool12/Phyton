from LibraryManagementSystem.Database.connection import get_connection

class BookModel:

    def get_all_books(self):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM books")
                return cursor.fetchall()
        finally:
            connection.close()

    def get_book(self, book_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM books WHERE book_id = %s"
                cursor.execute(sql, (book_id,))
                return cursor.fetchone()
        finally:
            connection.close()

    def add_book(self, title, author, description):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO books (title, author, description) VALUES (%s, %s, %s)"
                cursor.execute(sql, (title, author, description))
                connection.commit()
                return cursor.lastrowid
        finally:
            connection.close()

    def update_book(self, title, author, description, book_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE books SET title = %s, author = %s, description = %s WHERE id = %s"
                cursor.execute(sql, (title, author,description, book_id))
                connection.commit()
                return cursor.rowcount
        finally:
            connection.close()

    def delete_book(self, book_id):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM books WHERE id = %s"
                cursor.execute(sql, (book_id,))
                connection.commit()
                return cursor.rowcount
        finally:
            connection.close()
