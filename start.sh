#!/bin/bash
# apply DB Migrations
python manage.py migrate
# Debug development server
# no need for gnuicorn, also runserver better for debugging and "docker cp"
exec python manage.py runserver 0.0.0.0:8000
