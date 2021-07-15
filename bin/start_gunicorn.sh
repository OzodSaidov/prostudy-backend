#!/bin/bash
source /home/prostudy-backend/venv/bin/activate
exec gunicorn -c "/home/prostudy-backend/bin/gunicorn_conf.py" prostudy.wsgi

