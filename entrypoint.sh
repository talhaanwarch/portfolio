# python manage.py collectstatic &&
gunicorn main_app.wsgi:application --bind 0.0.0.0:8000