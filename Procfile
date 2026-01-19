web: gunicorn gram_panchayat.wsgi
release: python manage.py migrate
worker: python manage.py process_tasks
