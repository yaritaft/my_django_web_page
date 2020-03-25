 #!/bin/bash
cat .envdev > .env
mv docker-compose-only-test-purposes.yml docker-compose.yml
docker-compose down
docker-compose build
docker-compose up -d --remove-orphans
id_container=$(docker ps | grep my_django_web_page_web | cut -d " " -f 1)
docker exec -ti $id_container python manage.py makemigrations --noinput
docker exec -ti $id_container python manage.py migrate --noinput
docker exec -ti $id_container python manage.py load_dummy_data
docker exec -ti $id_container rm -r staticfiles
docker exec -ti $id_container python manage.py collectstatic --noinput
echo -e "\n\n\n\n\n\n\n\n==========\n\n\n"
echo "NOW CONTROL + CLICK OVER THIS URL - > http://127.0.0.1:8000"
echo "\n\n\n==========\n\n\n\n\n\n\n"
mv docker-compose.yml docker-compose-only-test-purposes.yml
