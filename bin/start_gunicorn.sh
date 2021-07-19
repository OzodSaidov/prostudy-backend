#!/bin/bash
source /home/prostudy/prostudy-backend/venv/bin/activate
exec gunicorn -c "/home/prostudy/prostudy-backend/bin/gunicorn_conf.py" prostudy.wsgi

