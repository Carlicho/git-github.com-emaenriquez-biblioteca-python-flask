from flask import Flask
from app.views import index, get_all_books, get_book, create_book, update_book, delete_book
from app.database import init_app

# Initializing the Flask app
app = Flask(__name__)

# Initialize the database
init_app(app)

# Route definitions
app.route('/', methods=['GET'])(index)
app.route('/api/books/', methods=['GET'])(get_all_books)
app.route('/api/books/', methods=['POST'])(create_book)
app.route('/api/books/<int:id_book>', methods=['GET'])(get_book)
app.route('/api/books/<int:id_book>', methods=['PUT'])(update_book)
app.route('/api/books/<int:id_book>', methods=['DELETE'])(delete_book)

if __name__ == '__main__':
    app.run(debug=True)
