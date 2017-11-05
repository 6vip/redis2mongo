#!/bin/bash

python manage.py celery worker -c 4 --loglevel=info
python manage.py runserver 0.0.0.0:8080