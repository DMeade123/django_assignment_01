
Build = docker compose build
Run = docker compose up -d (runs in detached mode)
.env = view .env example to set up .env and replace with correct credentials
migratations = Once docker container is running run docker compose exec web python manage.py migrate
Access App and Api = http://127.0.0.1/8000 or http://127.0.0.1/8000/api/book
