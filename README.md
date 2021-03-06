# Django REST Framework Example

This project is intended to showcase the capabilities of the Django REST Framework with a minimal amount of code.

## [Wiki](https://github.com/athento/drf-example/wiki)

Read the wiki for a complete project breakthrough and explanation.

Or, if you can figure it out for yourself, follow the steps below !

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

## Images

![api](https://raw.githubusercontent.com/athento/drf-example/master/img/api.png)

![method](https://raw.githubusercontent.com/athento/drf-example/master/img/method.png)

![docs](https://raw.githubusercontent.com/athento/drf-example/master/img/docs.png)
