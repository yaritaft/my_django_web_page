#!/bin/bash
cat .env > .envdev 
python3.7 manage.py collectstatic --noinput
git add .
git commit -m "$1"
git add .
git commit -m "$1"
git push
git push heroku master
