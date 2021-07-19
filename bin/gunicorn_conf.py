command = '/home/prostudy/prostudy-backend/venv/bin/gunicorn'
pythonpath = '/home/prostudy/prostudy-backend/prostudy'
bind = '127.0.0.1:8000'
workers = 5
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=prostudy.settings'

