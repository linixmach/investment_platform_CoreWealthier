web: gunicorn investment_platform.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate && python manage.py collectstatic --noinput