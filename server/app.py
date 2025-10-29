#!/usr/bin/env python3

from flask import request, session, jsonify, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

import os
from config import create_app, db, api
from models import Book, BookSchema

env = os.getenv("FLASK_ENV", "dev")
app = create_app(env)

class Books(Resource):
    def get(self):
        # Get pagination parameters from query string with defaults
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        
        # Use SQLAlchemy's paginate method
        paginated_books = Book.query.paginate(
            page=page,
            per_page=per_page,
            error_out=False  # Don't raise error if page is out of range
        )
        
        # Serialize the books using BookSchema
        books_data = [BookSchema().dump(book) for book in paginated_books.items]
        
        # Return structured response with pagination metadata
        response = {
            "page": paginated_books.page,
            "per_page": paginated_books.per_page,
            "total": paginated_books.total,
            "total_pages": paginated_books.pages,
            "items": books_data
        }
        
        return response, 200


api.add_resource(Books, '/books', endpoint='books')


if __name__ == '__main__':
    app.run(port=5555, debug=True)