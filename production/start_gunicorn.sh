#!/bin/bash
source /home/prostudy-backend/venv/bin/activate
exec gunicorn -c "/home/prostudy-backend/production/gunicorn_conf.py" prostudy.wsgi

