from app.database import get_db

class Book:

    # Constructor
    def __init__(self, id_book=None, book_title=None, author_name=None, publication_date=None, book_cover=None):
        self.id_book = id_book
        self.book_title = book_title
        self.author_name = author_name
        self.publication_date = publication_date
        self.book_cover = book_cover

    def serialize(self):
        return {
            'id_book': self.id_book,
            'title': self.book_title,
            'author': self.author_name,
            'release_date': self.publication_date,
            'banner': self.book_cover
        }
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM books"
        cursor.execute(query)
        rows = cursor.fetchall() 

        books = [Book(id_book=row[0], book_title=row[1], author_name=row[2], publication_date=row[3], book_cover=row[4]) for row in rows]

        cursor.close()
        return books

    @staticmethod
    def get_by_id(id_book):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM books WHERE id_book = %s", (id_book,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Book(id_book=row[0], book_title=row[1], author_name=row[2], publication_date=row[3], book_cover=row[4])
        return None
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_book:
            cursor.execute("""
                UPDATE books SET book_title = %s, author_name = %s, publication_date = %s, book_cover = %s
                WHERE id_book = %s
            """, (self.book_title, self.author_name, self.publication_date, self.book_cover, self.id_book))
        else:
            cursor.execute("""
                INSERT INTO books (book_title, author_name, publication_date, book_cover) VALUES (%s, %s, %s, %s)
            """, (self.book_title, self.author_name, self.publication_date, self.book_cover))
            self.id_book = cursor.lastrowid
        db.commit()
        cursor.close()