## Live Demo
A live demo is available at: https://url-shortener-take-home.onrender.com

`/api/books/` is pre-populated for testing

## App - Core (URL Shortener)
The `core` app is a URL shortener tool that creates short URLs and redirects from them to the specified target URL. It provides the following features:

- Generate random short URLS that are 10 characters long
- Allows users to specify an unused custom short URL (max 10 chars)
- Allows the originator of a custom short URL to modify the target of the short URL using a returned random PIN

## API - Books
The `books` app provides an API for listing books. It includes the following endpoints:

- `/api/books/` - GET: Retrieve a list of books.

In order to improve query times, results have been paginated and the following parameters have been enabled:
- `?page=X`: returns the requested page of results 
- `?page_size=X`: limits the number of entries per page of results (default: 10, max: 100)
- `?fields=[]`: limits the returned book data to the fields specified by a comma-seperated list
- `?exclude=[]`: excludes fields specified by a comma-seperated list from the returned book data; cannot be used in conjunction with `?fields`

eg. `/api/books/?page=3&page_size=5&fields=id,title` will return the third page of 5 results containing only the books' ids and titles

## Installation and Setup

To set up the project locally, follow these steps:

1. Clone the repository: 
```
git clone git@github.com:SUPERVISA-AI/url-shortener-take-home.git
```
2. Navigate to the project directory: 
```
cd url_shortener_take_home
```
3. Create and activate a virtual environment using `pipenv` (`requirements.txt` file provided in case that pipenv doesn't work):
```
pipenv install --dev
pipenv shell
```
4. Install project dependencies:
```
pipenv install
```
5. DB setup:

    5.1: Create `.env` file in the root of the project following the fields in `.env.example`
    
    5.2: Create a postgres database for this project
    
    5.3: Replace dummy values in `.env` file with your db credentials
6. Apply database migrations:
```
python manage.py migrate
```
7. Start the development server:
```
python manage.py runserver
```
8. Access the project in your web browser at `http://localhost:8000/`.

### Management Commands

This app includes the following management commands:

- `create_test_books <count>`: Creates test book instances for endpoint performance testing. If `count` is not provided, it defaults to 100.
```
python manage.py create_test_books 2000
```

- `clear_db`: Delete all book related instances from the database.
```
python manage.py clear_db
```
