from flask import Flask, jsonify
from flask_cors import CORS
from app.views import index, get_all_books, get_book, create_book, update_book, delete_book
from app.database import init_app

# Initializing the Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}) # Enable CORS for all routes

# Initialize the database
init_app(app)

# Route definitions
app.route('/', methods=['GET'])(index)
app.route('/api/books/', methods=['GET'])(get_all_books)
app.route('/api/books/', methods=['POST'])(create_book)
app.route('/api/books/<int:id_book>', methods=['GET'])(get_book)
app.route('/api/books/<int:id_book>', methods=['PUT'])(update_book)
app.route('/api/books/<int:id_book>', methods=['DELETE'])(delete_book)

# Decorador para registrar los encabezados de respuesta
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    print(f"Response headers: {response.headers}")  # Agregar registro de los encabezados de respuesta
    return response

if __name__ == '__main__':
    app.run(debug=True)