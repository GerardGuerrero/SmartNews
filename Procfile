release: python manage.py migrate --noinput
web: gunicorn SmartNewsProject.wsgi --log-level=info --log-file -
