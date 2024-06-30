from app.database import get_db

class Book:
    def __init__(self, id_book, book_title, author_name, publication_date, book_cover):
        self.id_book = id_book
        self.book_title = book_title
        self.author_name = author_name
        self.publication_date = publication_date
        self.book_cover = book_cover

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_book is None:
            cursor.execute(
                "INSERT INTO books (book_title, author_name, publication_date, book_cover) VALUES (%s, %s, %s, %s)",
                (self.book_title, self.author_name, self.publication_date, self.book_cover)
            )
            self.id_book = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE books SET book_title = %s, author_name = %s, publication_date = %s, book_cover = %s WHERE id_book = %s",
                (self.book_title, self.author_name, self.publication_date, self.book_cover, self.id_book)
            )
        db.commit()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        return [Book(*book) for book in books]

    @staticmethod
    def get_by_id(id_book):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books WHERE id_book = %s", (id_book,))
        book = cursor.fetchone()
        if book:
            return Book(*book)
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM books WHERE id_book = %s", (self.id_book,))
        db.commit()

    def serialize(self):
        return {
            'book_id': self.id_book,
            'book_title': self.book_title,
            'author_name': self.author_name,
            'publication_date': self.publication_date,
            'book_cover': self.book_cover
        }