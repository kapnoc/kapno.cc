release: python manage.py migrate && python manage.py compilemessages
web: gunicorn kapno_cc.wsgi --log-file -