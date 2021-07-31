command = '/usr/src/app/venv/bin/gunicorn'
pythonpath = '/usr/src/app/prostudy'
bind = '0.0.0.0:8000'
workers = 5
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=prostudy.settings'
