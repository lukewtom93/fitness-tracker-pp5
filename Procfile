release: python backend/manage.py makemigrations && python backend/manage.py migrate
web: PYTHONPATH=backend gunicorn api.wsgi