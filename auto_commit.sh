#!/bin/bash
cat .env > .envdev 
rm -r staticfiles
python3 manage.py collectstatic --noinput
git add .
git commit -m "$1"
git add .
git commit -m "$1"
git push
git push heroku master
