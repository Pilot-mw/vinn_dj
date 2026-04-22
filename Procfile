web: gunicorn djvin_site.wsgi --log-file -
release: python manage.py migrate && python manage.py createadmin