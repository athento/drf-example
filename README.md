# drf-example

This project is intended to showcase the capabilities of the Django REST Framework.

## Getting started

1. First, clone this repository:
  - `git clone https://github.com/athento/drf-example`
  - `cd drf-example`
2. Create a Python virtual environment, this step is optional, but recommended:
  - `pip install virtualenv`
  - `virtualenv env`
  - `source ./env/bin/activate`
3. Install the dependencies:
  - `pip install -r requirements.txt`
4. Run database migrations:
  - `python manage.py migrate`
5. Create a superuser:
  - `python manage.py createsuperuser`
6. Run the server:
  - `python manage.py runserver`
7. Browse the live example. Available URLs:
  - [/api](http://localhost:8000/api/)
  - [/api/token](http://localhost:8000/api/token/)
  - [/api/docs](http://localhost:8000/api/docs/)
8. Read the wiki:
  - [drf-example wiki](https://github.com/athento/drf-example/wiki)
