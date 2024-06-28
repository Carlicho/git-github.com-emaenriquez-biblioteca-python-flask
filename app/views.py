from flask import jsonify, request
from app.models import Book

def index():
    return "Cac Grupo 4 API Biblioteca"

def get_all_books():
    books = Book.get_all()
    books_serialized = [book.serialize() for book in books]
    return jsonify(books_serialized)

def get_book(book_id):
    book = Book.get_by_id(book_id)
    if book:
        return jsonify(book.serialize())
    return jsonify({"message": "Book not found"}), 404

def create_book():
    data = request.json
    new_book = Book(
        book_title=data['book_title'],
        author_name=data['author_name'],
        publication_date=data['publication_date'],
        book_cover=data['book_cover']
    )
    new_book.save()
    return jsonify({"message": "Libro creado con exito"})