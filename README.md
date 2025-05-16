# django_assingment_01


    The chosen application domain (e.g., E-commerce, Library).
        Library Management System

    How to set up the project (create virtual env, install requirements).
        python -m venv venv
        venv/Scripts/Activte
        pip install -r requirements.txt

    How to create a .env file based on .env.example and fill in actual database credentials.

    Right Click and Select new file under project directory
    Example of .env file

SECRET_KEY='your-super-secret-django-key-here!@#$%^&*(-+=)'

DEBUG=TRUE
FORMAT FOR POSTGRES

    DATABASE_URL='postgres://your_db_user:your_db_password@localhost:5432/your_db_name'

    How to run migrations ($ python manage.py migrate). How to create a superuser ($ python manage.py createsuperuser) and run the development server ($ python manage.py runserver). (Use PS> prefix for PowerShell commands if applicable).
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser (follow prompted credentials)
        python manage.py runserver
Part1 README
