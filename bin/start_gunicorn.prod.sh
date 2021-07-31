#!/bin/bash
source /usr/src/app/venv/bin/activate
exec gunicorn -c "/usr/src/app/bin/gunicorn_conf.py" prostudy.wsgi