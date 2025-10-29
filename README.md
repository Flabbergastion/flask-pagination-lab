# Lab: Flask Pagination

## Introduction

✅ **COMPLETED** - This project has successfully implemented server-side pagination for a Flask API endpoint. The `/books` endpoint now supports efficient pagination instead of returning all books at once, which improves performance and provides a better user experience.

**Implemented Features:**
* ✅ Accept `?page` and `?per_page` query parameters
* ✅ Return only a subset of records using SQLAlchemy's `.paginate()` method
* ✅ Include comprehensive metadata (total, page, total_pages, per_page) in the response
* ✅ Handle edge cases gracefully (invalid pages, empty results)
* ✅ All tests passing

This implementation follows industry standards used by APIs across the web from Shopify to Reddit to GitHub.

## Tools & Resources

- [GitHub Repo](https://github.com/learn-co-curriculum/flask-pagination-lab)
- [Flask SQLAlchemy Docs - paginate](https://flask-sqlalchemy.readthedocs.io/en/stable/pagination/)

## Set Up

The starter code includes a Flask app and seed data for books.

To get started:

```bash
pipenv install && pipenv shell
cd server
flask db init
flask db migrate -m "initial migration"
flask db upgrade head
python seed.py
python app.py
```

You can view the API in your browser or using Postman. Test pagination by visiting
http://localhost:5555/books?page=1&per_page=5.

## Implementation Details

### ✅ Completed Implementation

The pagination feature has been successfully implemented with the following components:

#### API Endpoint: `/books`

**Query Parameters:**
- `page` (integer, default: 1) - Page number to retrieve
- `per_page` (integer, default: 5) - Number of items per page

**Response Format:**
```json
{
  "page": 1,
  "per_page": 5,
  "total": 500,
  "total_pages": 100,
  "items": [
    {
      "id": 1,
      "title": "Example Book Title",
      "author": "Author Name", 
      "description": "Book description"
    }
  ]
}
```

#### Usage Examples

- `GET /books` - Returns first 5 books (default pagination)
- `GET /books?page=2&per_page=10` - Returns books 11-20 (10 per page)
- `GET /books?page=1&per_page=3` - Returns first 3 books
- `GET /books?page=999` - Returns empty results gracefully

#### Key Features

✅ **SQLAlchemy Pagination**: Uses `.paginate()` method for efficient database queries  
✅ **Error Handling**: Gracefully handles invalid pages without crashing  
✅ **Flexible Parameters**: Supports custom page sizes and navigation  
✅ **Complete Metadata**: Includes all necessary pagination information  
✅ **Test Coverage**: All test cases pass successfully  

### Testing

Run the test suite to verify functionality:
```bash
cd server
pipenv run pytest testing/pagination_test.py -v
```

All tests pass:
- Default pagination behavior
- Custom page and per_page parameters  
- Edge cases (empty pages, invalid ranges)
- Metadata accuracy

## Submit Solution

CodeGrade will use the same test suite as the test suite included.

Once all tests are passing, commit and push your work using `git` to submit to CodeGrade through Canvas.
