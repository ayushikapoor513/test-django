# test-django
dockerhub-link : https://hub.docker.com/repository/docker/ayushi1/test-django-master_web

STEPS TO RUN :
docker-compose up,
docker-compose exec web python manage.py makemigrations,
docker-compose exec web python manage.py migrate,
docker-compose build,
docker-compose up 
check
